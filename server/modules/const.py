#!usr/bin/env python
# _*_ coding:utf-8 _*_


class Const(object):
    """the error code"""

    SUCCESS = 1200
    MISSPARAM = 1202
    LOGIN_FAILED = 1203
    INNER_ERROR = 2006


class Msg(object):
    """the msg of the error code"""

    msg = {
        1200: "SUCCESS",
        1202: "MISSPARAM",
        1203: "NO_REGISTER",
        2006: "INNER_ERROR"
    }
