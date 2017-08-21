#!usr/bin/env python
# _*_ coding:utf-8 _*_

from marshmallow import Schema, fields, validate


class RegisterForm(Schema):
    """the register form"""

    username = fields.Str(validate=validate.Length(max=32), required=True)
    phone = fields.Str(validate=validate.Length(equal=11), required=True)
    sex = fields.Str()
    password = fields.Str(validate=validate.Length(max=32), required=True)
