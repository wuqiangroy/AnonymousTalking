#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import jsonify
from .const import Msg


def make_response(status=1200, data=None):
    return jsonify({
        "code": status,
        "msg": Msg.msg[status],
        "data": data
    })
