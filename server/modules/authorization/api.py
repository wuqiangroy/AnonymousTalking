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
    if not form.validate():
        return make_response(status=Const.MISSPARAM, data=None)
    phone = form.phone.data
    password = form.password.data
    user = User.objects(phone=phone).first()
    if user is not None and user.verity_password(password):
        res = {
            "token": user.token,
            "username": user.username,
            "phone": user.phone
        }
        return make_response(data=res)
    else:
        return make_response(status=1203)
