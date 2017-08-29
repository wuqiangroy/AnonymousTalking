#!usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
from uuid import uuid4
from flask import request

from . import user
from .model import User
from .controller import *
from ..const import Const
from ..functions import make_response


@user.route("/create_user", methods=["POST"])
def register():
    form = RegisterForm(request.form)
    if not form.validate():
        return make_response(Const.MISSPARAM, None)
    try:
        User(
            username=form.username.data,
            phone=form.phone.data,
            sex=form.sex.data,
            password=form.password.data,
            token=str(uuid4()).replace("-", "")
        ).save()
        res = {
            "username": form.username.data,
            "phone": form.phone.data,
            "sex": form.sex.data
        }
        return make_response(data=res)
    except Exception as e:
        logging.debug("[REGISTER][BUG|{}]".format(str(e)))
        return make_response(status=2006)
