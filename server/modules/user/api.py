#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import request

from . import user
from .controller import *
from ..const import Const
from ..functions import make_response


@user.route("/register", methods=["POST"])
def register():
    form = RegisterForm(request.form)
    if not form:
        return make_response(Const.MISSPARAM, None)


