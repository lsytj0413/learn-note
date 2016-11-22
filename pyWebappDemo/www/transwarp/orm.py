# coding=utf-8

"""
数据库ORM模块
"""

import logging


_triggers = frozenset(['pre_insert', 'pre_update', 'pre_delete'])


def _gen_sql(table_name, mappings):
    """
    构造建表sql语句
    """
    pk = None
    sql = ['-- generating SQL for {}:'.format(table_name), 'create table `%s`('%(table_name)]
    for f in sorted(mappings.values(), lambda x, y: cmp(x._order, y._order)):
        if not hasattr(f, 'ddl'):
            raise StandardError('no ddl in field "{}"'.format(f))
        ddl = f.ddl
        nullable = f.nullable
        if f.primary_key:
            pk = f.name
        sql.append(nullable and '  `%s` %s,' % (f.name, ddl) or '  `%s` %s not null,' % (f.name, ddl))
    sql.append('  primary key(`{}`)'.format(pk))
    sql.append(');')
    return '\n'.join(sql)


class ModelMetaclass(type):
    """
    ORM模型元类
    """

    def __new__(cls, name, bases, attrs):
        if name == 'Modle':
            return type.__new__(cls, name, bases, attrs)
        if not hasattr(cls, 'subclasses'):
            cls.subclasses = {}
        if not name in cls.subclasses:
            cls.subclasses[name] = name
        else:
            logging.warning('Redefine class: {}'.format(name))

        mappings = dict()
        primary_key = None
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                if not v.name:
                    v.name = k
                if v.primary_key:
                    if primary_key:
                        raise TypeError('Cannot define more than 1 primary key in class: {}'.format(name))
                    if v.updatable:
                        v.updatable = False
                    if v.nullable:
                        v.nullable = False
                    primary_key = v
                mappings[k] = v

        if not primary_key:
            raise TypeError('Primary key not defined in class: {}'.format(name))
        for k in mappings.iterkeys():
            attrs.pop(k)
        if not '__table__' in attrs:
            attrs['__table__'] = name.lower()
        attrs['__mappings__'] = mappings
        attrs['__primary_key__'] = primary_key
        attrs['__sql__'] = lambda self: __gen_sql(attrs['__table__'], mappings)
        for trigger in _triggers:
            if not trigger in attrs:
                attrs[trigger] = None
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    """
    ORM基类
    """

    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'dict' object has no attribute '{}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value
