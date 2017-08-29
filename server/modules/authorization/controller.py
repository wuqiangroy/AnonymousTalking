#!usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField, validators
from wtforms.validators import Regexp, Length, EqualTo


class CreateTokenForm(Form):
    """the login form"""

    phone = StringField("phone", [Regexp(r"^1\d{10}")])
    password = StringField("password", [Length(1, 32)])


class ChangeTokenForm(Form):
    """the change password form"""

    old_password = StringField("old_password", [Length(1, 32)])
    new_password = StringField("new_password", [Length(1, 32)])
    new_password2 = StringField("new_password2", [Length(1, 32)])
