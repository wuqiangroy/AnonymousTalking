#!usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField
from wtforms.validators import required, Length


class LoginForm(Form):
    """the login form"""

    phone = StringField("phone", [required(), Length(11)])
    password = StringField("password", [required(), Length(1, 64)])
