#!usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
import logging.config
from time import time

conf = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
        'format': ('[%(asctime)s.%(msecs).03d] [%(levelname)s] '
                   '[pid|%(process)d] [%(name)s:%(lineno)d] %(message)s'),
            'datefmt': '%m-%d %H:%M:%S'
    },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'app': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

logging.config.dictConfig(conf)
levelnames = logging._levelToName

# create logger
project_logger = logging.getLogger('server')


def class_logger(cls):
    cls.logger = project_logger.getChild(cls.__name__)
    return cls


def update_record(record, level, msg, *args):
    record.levelno = level
    record.levelname = levelnames[level]
    record.msg = msg
    record.args = args
    ct = time()
    record.created = ct
    record.msecs = (ct - ct) * 1000
