#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint, request, jsonify
from .const import Msg


def make_response(status=1200, data=None):
    return jsonify({
        "code": status,
        "msg": Msg.msg[status],
        "data": data
    })


class BaseBlueprint(Blueprint):

    def post(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            form = options.pop("form", None)
            if not form:
                return "POST methods must contain params"
            form.validate(request.form)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
