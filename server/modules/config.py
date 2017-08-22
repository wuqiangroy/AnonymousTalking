#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """基础配置"""

    SECRET_KEY = os.environ.get("secret_key") or "coding change world"

    @staticmethod
    def init_app(app):
        pass


class Development(BaseConfig):
    """开发配置"""

    DEBUG = True
    MONGODB_URL = ""
    REDIS_URL = ""


class Production(BaseConfig):
    """线上配置"""

    MONGODB_URL = ""
    REDIS_URL = ""

Config = {
    "development": Development,
    "production": Production,
    "default": Development
}
