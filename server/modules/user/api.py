#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import jsonify, request
from flask.views import MethodView

from .controller import *
from ..const import Const, Msg
from .model import User


class BaseView(MethodView):
    def dispatch_request(self, *args, **kwargs):
        status, data = super(BaseView, self).dispatch_request(*args, **kwargs)
        return jsonify({
            "code": status,
            "msg": Msg.msg[status],
            "data": data
        })


class Login(BaseView):
    """login view"""

    def post(self):
        form = LoginForm(request.form)
        if not form:
            return Const.MISSPARAM, None
        phone = form.get("phone")
        password = form.get("password")
        user = User.objects(phone=phone).first()
        if not user:
            return Const.NO_REGISTER, None
