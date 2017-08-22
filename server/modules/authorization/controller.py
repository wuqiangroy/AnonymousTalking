#!usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField, validators


class LoginForm(Form):
    """the login form"""

    phone = StringField("phone", [validators.Regexp(r"^1\d{10}")])
    password = StringField("password", [validators.Length(1, 32)])
