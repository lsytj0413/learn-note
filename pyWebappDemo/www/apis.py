# coding=utf-8

"""
JSON Api 定义模块
"""

import re, json, logging, functools

from transwarp.web import ctx


def dumps(obj):
    return json.dumps(obj)


class APIError(StandardError):
    """
    API Error 基类
    """

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data


class APIValueError(APIError):
    """
    value错误类
    """

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFountError(APIError):
    """
    资源文件不存在 错误类
    """

    def __init__(self, field, message=''):
        super(APIResourceNotFountError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    """
    没有访问权限 错误类
    """

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
