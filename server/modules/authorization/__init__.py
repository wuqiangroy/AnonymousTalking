#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint

authorization = Blueprint("authorization", __name__)

from . import api
