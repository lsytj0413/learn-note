# coding=utf-8

"""
公共库
"""


class Dict(dict):
    """
    自定义字典对象, 支持x.y访问方式
    """

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '{}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value


def to_str(s):
    """
    将s转换为str.
    """
    if isinstance(s, str):
        return s
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return str(s)


def to_unicode(s, encoding='utf-8'):
    """
    将s转换为unicode.
    """
    return s.decode('utf-8')


