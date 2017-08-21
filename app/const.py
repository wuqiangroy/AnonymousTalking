#!usr/bin/env python
# _*_ coding:utf-8 _*_


class Const(object):
    """the error code"""

    SUCCESS = 1200
    MISSPARAM = 1202


class Msg(object):
    """the msg of the error code"""

    msg = {
        1200: "SUCCESS",
        1202: "MISSPARAM"
    }
