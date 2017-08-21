#!usr/bin/env python
# _*_ coding:utf-8 _*_

from mongoengine import DynamicDocument, StringField


class User(DynamicDocument):
    """user table"""

    username = StringField(max_length=64, required=True)
    phone = StringField(max_length=11, min_length=11, required=True)
    sex = StringField(required=True)
    password = StringField(max_length=64, required=True)
