# coding=utf-8

"""
统一配置文件
"""

import config_default
from transwarp.common import Dict


def merge(defaults, override):
    r = {}
    for k, v in defaults.iteritems():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def to_dict(d):
    D = Dict()
    for k, v in d.iteritems():
        D[k] = to_dict(v) if isinstance(v, dict) else v
    return D


configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass


configs = to_dict(configs)
