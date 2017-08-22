#!usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField, validators


class RegisterForm(Form):
    """the register form"""

    username = StringField("username", [validators.Length(1, 32)])
    phone = StringField("phone", [validators.Regexp(r"^1\d{10}")])
    sex = StringField()
    password = StringField("password", [validators.Length(1, 32)])
