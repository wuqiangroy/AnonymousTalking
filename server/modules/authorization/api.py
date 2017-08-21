#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import request

from . import authorization
from .controller import *
from ..const import Const
from ..functions import make_response
from ..user.model import User


@authorization.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)
    if not form:
        return make_response(status=Const.MISSPARAM, data=None)
    phone = form.get("phone")
    password = form.get("password")
    user = User.objects(phone=phone).first()
    if not user:
        return make_response(status=Const.NO_REGISTER, data=None)
