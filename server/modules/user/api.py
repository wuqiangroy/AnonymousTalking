#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import jsonify, request
from flask.views import MethodView

from . import user
from .controller import *
from ..const import Const, Msg
from .model import User


def make_response(status=1200, data=None):
    return jsonify({
        "code": status,
        "msg": Msg.msg[status],
        "data": data
    })


@user.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)
    if not form:
        return make_response(status=Const.MISSPARAM, data=None)
    phone = form.get("phone")
    password = form.get("password")
    user = User.objects(phone=phone).first()
    if not user:
        return make_response(status=Const.NO_REGISTER, data=None)
