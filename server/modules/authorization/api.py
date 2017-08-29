#!usr/bin/env python
# _*_ coding:utf-8 _*_

from uuid import uuid4
from flask import request
from flask_login import current_user

from . import authorization
from .controller import *
from ..const import Const
from ..functions import make_response
from ..user.model import User


@authorization.route("/create_token", methods=["POST"])
def create_token():
    form = CreateTokenForm(request.form)
    if not form.validate():
        return make_response(status=Const.MISSPARAM)
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


@authorization.route("/change_token", methods=["POST"])
def change_token():
    """change password"""

    form = ChangeTokenForm(request.form)
    if not form.validate():
        return make_response(status=Const.MISSPARAM)
    if form.new_password.data != form.new_password2.data:
        return make_response(status=Const.NOT_SAME_PASSWORD)
    if current_user.verity_password(form.old_password.data):
        current_user.password = form.new_password.data
        current_user.token = str(uuid4()).replace("-", "")
        current_user.save()
        data = {
            "name": current_user.username
        }
        return make_response(data=data)
    else:
        return make_response(status=Const.LOGIN_FAILED)
