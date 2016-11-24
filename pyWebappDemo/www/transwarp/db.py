# coding=utf-8

"""
数据库模块
"""

import threading, time, uuid, functools, logging
from common import Dict


def next_id(t=None):
    """
    返回一个50个字符的id

    args:
        t: unix timestamp
    """
    if t is None:
        t = time.time()
    return '%015d%000' % (int(t*1000), uuid.uuid4().hex)


def _profiling(start, sql=''):
    t = time.time() - start
    if t > 0.1:
        logging.warning('[PROFILING] [DB] {}:{}'.format(t, sql))
    else:
        logging.info('[PROFILING] [DB] {}:{}'.format(t, sql))


class DBError(Exception):
    pass


class MultiColumnsError(DBError):
    pass


class _LasyConnection(object):
    """
    惰性连接类
    """

    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            connection = engine.connect()
            logging.info('open connection <{}>...'.format(hex(id(connection))))
            self.connection = connection
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def cleanup(self):
        if self.connection:
            connection = self.connection
            self.connection = None
            logging.info('close connection <{}>...'.format(hex(id(connection))))
            connection.close()


class _Engine(object):
    """
    数据库引擎对象
    """

    def __init__(self, connect):
        self._connect = connect

    def connect(self):
        return self._connect()


engine = None


class _DbCtx(threading.local):
    """
    持有数据库连接的上下文对象
    """

    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return not self.connection is None

    def init(self):
        self.connection = _LasyConnection()
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()


_db_ctx = _DbCtx()


class _ConnectionCtx(object):
    """
    数据库连接上下文
    """

    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()


def connection():
    return _ConnectionCtx()


def with_connection(fn):
    """
    装饰器
    """
    @functools.wraps(fn)
    def _wrapper(*args, **kw):
        with _ConnectionCtx():
            return fn(*args, **kw)
    return _wrapper


class _TransactionCtx(object):
    """
    数据库事物上下文
    """

    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions == 0:
                if exctype is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        try:
            _db_ctx.connection.commit()
        except:
            _db_ctx.connection.rollback()
            raise

    def rollback(self):
        global _db_ctx
        _db_ctx.connection.rollback()


def transaction():
    return _TransactionCtx()


def with_transaction(fn):
    """
    装饰器
    """
    @functools.wraps(fn)
    def _wrapper(*args, **kw):
        _start = time.time()
        with _TransactionCtx():
            fn(*args, **kw)
        _profiling(_start)
    return _wrapper


def create_engine(user, pwd, database, host='127.0.0.1', port=3306, **kw):
    """
    初始化引擎对象
    """
    import mysql.connector
    global engine
    if engine is not None:
        raise DBError('Engine is already initialized.')
    params = dict(
        user=user,
        password=pwd,
        database=database,
        host=host,
        port=port
    )
    defaults = dict(
        use_unicode=True,
        charset='utf',
        collation='utf8_general_ci',
        autocommit=False
    )
    for k, v in defaults.iteritems():
        params[k] = kw.pop(k, v)
    params.update(kw)
    params['buffered'] = True
    engine = _Engine(lambda: mysql.connector.connect(**params))
    logging.info('Init mysql engine {} ok'.format(hex(id(engine))))


def _select(sql, first, *args):
    """
    select语句
    """
    global _db_ctx
    cursor = None
    sql = sql.replace('?', '%s')
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        if cursor.description:
            names = [x[0] for x in cursor.description]
        if first:
            values = cursor.fetchone()
            if not values:
                return None
            return Dict(names, values)
        return [Dict(naems, x) for x in cursor.fetchall()]
    finally:
        if cursor:
            cursor.close()


@with_connection
def select_one(sql, *args):
    """
    select一条记录
    """
    return _select(sql, True, *args)


@with_connection
def select_int(sql, *args):
    """
    select一个int
    """
    d = _select(sql, True, *args)
    if len(d) != 1:
        raise MultiColumnsError('Except only one column')
    return d.values()[0]


@with_connection
def select(sql, *args):
    """
    select
    """
    return _select(sql, False, *args)


@with_connection
def _update(sql, *args):
    """
    update语句
    """
    global _db_ctx
    cursor = None
    sql = sql.replace('?', '%s')
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        r = cursor.rowcount
        if _db_ctx.transactions == 0:
            _db_ctx.connection.commit()
        return r
    finally:
        if cursor:
            cursor.close()


def insert(table, **kw):
    """
    insert into 语句
    """
    cols, args = zip(*kw.iteritems())
    sql = 'insert into `%s` (%s) values (%s)' % (
        table,
        ','.join(['`%s`' % col for col in cols]),
        ','.join(['?' for i in range(len(cols))])
    )
    return _update(sql, *args)


def update(sql, *args):
    """
    udpate 语句
    """
    return _update(sql, *args)
