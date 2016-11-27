# coding=utf-8

"""
WEB framework
"""


import types, os, re, cgi, sys, time, datetime, functools, mimetypes, threading, urllib
import logging, traceback

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from common import Dict, to_str, to_unicode


ctx = threading.local()

_TIMEDELTA_ZERO = datetime.timedelta(0)

_RE_TZ = re.compile('^([\+\-])([0-9]{1,2})\:([0-9]{1,2})$')


class UTC(datetime.tzinfo):
    """
    UTC
    """

    def __init__(self, utc):
        utc = str(utc.strip().upper())
        mt = _RE_TZ.match(utc)
        if mt:
            minus = mt.group(1)=='-'
            h = int(mt.group(2))
            m = int(mt.group(3))
            if minus:
                h, m = (-h), (-m)
            self._utcoffset = datetime.timedelta(hours=h, minutes=m)
            self._tzname = 'UTC%s' % (utc)
        else:
            raise ValueError('bad utc time zone')

    def utcoffset(self, dt):
        return self._utcoffset

    def dst(self, dt):
        return _TIMEDELTA_ZERO

    def tzname(self, dt):
        return self._tzname

    def __str__(self):
        return 'UTC tzinfo object (%s)' % (self._tzname)

    __repr__ = __str__


_RESPONSE_STATUSES = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',

    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi Status',
    226: 'IM Used',

    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: 'Temporary Redirect',

    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Noe Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    418: "I'm a teapot",
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    426: 'Upgrade Required',

    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    507: 'Insufficient Storage',
    510: 'Not Extended',
}


_RE_RESPONSE_STATUS = re.compile(r'^\d\d\d(\ [\w\ ]+)?$')


_RESPONSE_HEADERS = (
    'Accept-Ranges',
    'Age',
    'Allow',
    'Cache-Control',
    'Connection',
    'Content-Encoding',
    'Content-Language',
    'Content-Length',
    'Content-Location',
    'Content-MD5',
    'Content-Disposition',
    'Content-Range',
    'Content-Type',
    'Date',
    'ETag',
    'Expires',
    'Last-Modified',
    'Link',
    'Location',
    'P3P',
    'Pragma',
    'Proxy-Authenticate',
    'Refresh',
    'Retry-After',
    'Server',
    'Set-Cookie',
    'Strict-Transport-Security',
    'Trailer',
    'Transfer-Encoding',
    'Vary',
    'Via',
    'Warning',
    'WWW-Authenticate',
    'X-Frame-Options',
    'X-XSS-Protection',
    'X-Content-Type-Options',
    'X-Forwarded-Proto',
    'X-Powered-By',
    'X-UA-Compatible',
)


_RESPONSE_HEADER_DICT = dict(zip(map(lambda x: x.upper(), _RESPONSE_HEADERS),
                                 _RESPONSE_HEADERS
))


_HEADER_X_POWERED_BY = ('X-Powered-By', 'transwarp/1.0')


class HttpError(Exception):
    """
    错误类
    """

    def __init__(self, code):
        super(HttpError, self).__init__()
        self.status = '%d %s' % (code, _RESPONSE_STATUSES[code])

    def header(self, name, value):
        if not hasattr(self, '_headers'):
            self._headers = [_HEADER_X_POWERED_BY]
        self._headers.append((name, value))

    @property
    def headers(self):
        if hasattr(self, '_headers'):
            return self._headers
        return []

    def __str__(self):
        return self.status

    __repr__ = __str__


class RedirectError(HttpError):
    """
    重定向错误
    """

    def __init__(self, code, location):
        super(RedirectError, self).__init__(code)
        self.location = location

    def __str__(self):
        return '%s, %s' % (self.status, self.location)

    __repr__ = __str__


def badrequest():
    """
    Bad Request Response.
    """
    return HttpError(400)


def unauthorized():
    """
    Unauthorized Response.
    """
    return HttpError(401)


def forbidden():
    """
    Forbidden Response.
    """
    return HttpError(403)


def notfound():
    """
    Not Found Response.
    """
    return HttpError(404)


def conflict():
    """
    Conflict Response.
    """
    return HttpError(409)


def internalerror():
    """
    Internal Error Response.
    """
    return HttpError(500)


def redirect(location):
    """
    Redirect Response.
    """
    return RedirectError(301, location)


def found(location):
    """
    Temporary Redirect Response.
    """
    return RedirectError(302, location)


def seeother(location):
    """
    Temporary Redirect Response.
    """
    return RedirectError(303, location)


def quote(s, encoding='utf-8'):
    """
    将url转换为str.
    """
    if isinstance(s, unicode):
        s = s.encode(encoding)
    return urllib.quote(s)


def unquote(s, encoding='utf-8'):
    """
    将url unquote为unicode.
    """
    return urllib.unquote(s).decode(encoding)


def get(path):
    """
    GET请求的装饰器
    """
    def _decorator(func):
        func.__web_route__ = path
        func.__web_method__ = 'GET'
        return fnnc
    return _decorator


def post(path):
    """
    POST请求的装饰器
    """
    def _decorator(func):
        func.__web_route__ = path
        func.__web_method__ = 'POST'
        return fnnc
    return _decorator


_re_route = re.compile(r'(\:[a-zA-Z_]\w*)')


def _build_regex(path):
    """
    将urlpath转换为正则表达式
    """
    re_list = ['^']
    var_list = []
    is_var = False
    for v in _re_route.split(path):
        if is_var:
            var_name = v[1:]
            var_list.append(var_name)
            re_list.append(r'(?P<%s>[^\/]+)' % (var_name))
        else:
            s = ''
            for ch in v:
                if ch >= '0' and ch <= '9':
                    s = s + ch
                elif ch  >= 'A' and ch <= 'Z':
                    s = s + ch
                elif ch  >= 'a' and ch <= 'z':
                    s = s + ch
                else:
                    s = s + '\\' + ch
            re_list.append(s)
        is_var = not is_var
    re_list.append('$')
    return ''.join(re_list)


class Route(object):
    """
    路由类
    """

    def __init__(self, func):
        self.path = func.__web_route__
        self.method = func.__web_method__
        self.is_static = _re_route.search(self.path) is None
        if not self.is_static:
            self.route = re.compile(_build_regex(self.path))
        self.func = func

    def match(self, url):
        m = self.route.match(url)
        if m:
            return m.groups()
        return None

    def __call__(self, *args):
        return self.func(*args)

    def __str__(self):
        if self.is_static:
            return 'Route(static, %s, path=%s)' % (self.method, self.path)
        return 'Route(dynamic, %s, path=%s)' % (self.method, self.path)

    __repr__ = __str__


def _static_file_generator(fpath):
    BLOCK_SIZE = 8192
    with open(fpath, 'rb') as f:
        block = f.read(BLOCK_SIZE)
        while block:
            yield block
            block = f.read(BLOCK_SIZE)


class StaticFileRoute(object):
    """
    静态文件路由类
    """

    def __init__(self):
        self.method = 'GET'
        self.is_static = False
        self.route = re.compile('^/static/(.+)$')

    def match(self, url):
        if url.startswith('/static'):
            return (url[1:], )
        return None

    def __call__(self, *args):
        fpath = os.path.join(ctx.application.document_root, args[0])
        if not os.path.isfile(fpath):
            raise notfound()
        fext = os.path.splitext(fpath)[1]
        ctx.response.content_type = mimetypes.types_map.get(fext.lower(), 'application/octet-stream')
        return _static_file_generator(fpath)


def favicon_handler():
    return static_file_handler('/favicon.ico')


class MultipartFile(object):
    """
    多部分文件
    """

    def __init__(self, storage):
        self.filename = to_unicode(storage.filename)
        self.file = storage.file


class Request(object):
    """
    请求结构
    """

    def __init__(self, environ):
        self._environ = environ

    def _parse_input(self):
        def _convert(item):
            if isinstance(item, list):
                return [to_unicode(i.value) for i in item]
            if item.filename:
                return MultipartFile(item)
            return to_unicode(item.value)
        fs = cgi.FieldStorage(fp=self._environ['wsgi.input'],
                              environ=self._environ,
                              keep_blank_values = True
        )
        inputs = dict()
        for key in fs:
            inputs[key] = _convert(fs[key])
        return inputs

    def _get_raw_input(self):
        if not hasattr(self, '_raw_input'):
            self._raw_input = self._parse_input
        return self._raw_input

    def __getitem__(self, key):
        r = self._get_raw_input()[key]
        if isinstance(r, list):
            return r[0]
        return r

    def get(self, key, default=None):
        r = self._get_raw_input().get(key, default)
        if isinstance(r, list):
            return r[0]
        return r

    def gets(self, key):
        r = self._get_raw_input()[key]
        if isinstance(r, list):
            return r[:]
        return [r]

    def input(self, **kw):
        copy = Dict(**kw)
        raw = self._get_raw_input()
        for k, v in raw.iteritems():
            copy[k] = v[0] if isinstance(v, list) else v
        return copy

    def get_body(self):
        fp = self._environ['wsgi.input']
        return fp.read()

    @property
    def remote_addr(self):
        return self._environ.get('REMOTE_ADDR', '0.0.0.0')

    @property
    def document_root(self):
        return self._environ.get('DOCUMENT_ROOT', '')

    @property
    def query_string(self):
        return self._environ.get('QUERY_STRING', '')

    @property
    def environ(self):
        return self._environ

    @property
    def request_method(self):
        return self._environ['REQUEST_METHOD']

    @property
    def path_info(self):
        return urllib.unquote(self._environ.get('PATH_INFO', ''))

    @property
    def host(self):
        return self._environ.get('HTTP_HOST', '')

    def _get_headers(self):
        if not hasattr(self, '_headers'):
            hdrs = {}
            for k, v in self._environ.iteritems():
                if k.startwith('HTTP_'):
                    hdrs[k[5:].replace('_', '-').upper()] = v.decode('utf-8')
            self._headers = hdrs
        return self._headers

    @property
    def headers(self):
        return dict(**self._get_headers())

    def _get_cookies(self):
        if not hasattr(self, '_cookies'):
            cookies = {}
            cookie_str = self._environ.get('HTTP_COOKIE')
            if cookie_str:
                for c in cookie_str.split(';'):
                    pos = c.find('=')
                    if pos > 0:
                        cookies[c[:pos].strip()] = _unquote(c[pos+1:])
            self._cookies = cookies
        return self._cookies

    @property
    def cookies(self):
        return Dict(**self._get_cookies())

    def cookie(self, name, default=None):
        return self._get_cookies().get(name, default)


UTC_0 = UTC('+00:00')


class Response(object):
    """
    应答结构.
    """

    def __init__(self):
        self._status = '200 OK'
        self._headers = {
            'CONTENT-TYPE': 'text/html; charset=utf-8'
        }

    @property
    def headers(self):
        L = [[_RESPONSE_HEADER_DICT.get(k, k), v] for k, v in self._headers.iteritems()]
        if hasattr(self, '_cookies'):
            for v in self._cookies.itervalues():
                L.append(('Set-Cookie', v))
        L.append(_HEADER_X_POWERED_BY)
        return L

    def header(self, name):
        key = name.upper()
        if not key in _RESPONSE_HEADER_DICT:
            key = name
        return self._headers.get(key)

    def unset_header(self, name):
        key = name.upper()
        if not key in _RESPONSE_HEADER_DICT:
            key = name
        if key in self._headers:
            del self._headers[key]

    def set_header(self, name, value):
        key = name.upper()
        if not key in _RESPONSE_HEADER_DICT:
            key = name
        self._headers[key] = to_str(value)
