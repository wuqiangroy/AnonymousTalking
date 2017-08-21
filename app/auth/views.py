#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import jsonify
from flask.views import MethodView

from .. import const


class BaseView(MethodView):
    def dispatch_request(self, *args, **kwargs):
        status, data = super(BaseView, self).dispatch_request(*args, **kwargs)

        return jsonify({
            "code": status,
            "msg": const.get(status),
            "data": data
        })
