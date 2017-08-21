#!usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField
from wtforms.validators import required, Length


class RegisterForm(Form):
    """the register form"""

    username = StringField("username", [required(), Length(1, 64)])
    phone = StringField("phone", [required(), Length(11)])
    sex = StringField("sex", [required()])
    password = StringField("password", [required()])
