#!usr/bin/env python
# _*_ coding:utf-8 _*_

from datetime import datetime
from mongoengine import DynamicDocument, StringField, DateTimeField
from werkzeug.security import generate_password_hash, check_password_hash


class User(DynamicDocument):
    """user table"""

    username = StringField(max_length=64, required=True)
    phone = StringField(max_length=11, min_length=11, required=True)
    sex = StringField(required=True)
    password_hash = StringField(max_length=32, required=True)
    token = StringField(max_length=32, required=True)
    register_time = DateTimeField(default=datetime.utcnow)
    login_time = DateTimeField(default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verity_password(self, password):
        return check_password_hash(self.password_hash, password)
