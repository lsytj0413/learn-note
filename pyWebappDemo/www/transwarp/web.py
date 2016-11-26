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
