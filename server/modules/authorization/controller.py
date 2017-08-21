#!usr/bin/env python
# _*_ coding:utf-8 _*_

from marshmallow import Schema, fields, validate


class LoginForm(Schema):
    """the login form"""

    phone = fields.Str(validate=validate.Length(equal=11), required=True)
    password = fields.Str(validate=validate.Length(max=32), required=True)
