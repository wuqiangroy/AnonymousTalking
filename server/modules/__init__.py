#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask
from flask_login import LoginManager

from .config import Config

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"


def create_app(config="development"):
    """create app"""

    app = Flask(__name__)
    app.config.from_object(Config[config])
    Config[config].init_app(app)
    login_manager.init_app(app)

    from .user import user
    from .authorization import authorization
    app.register_blueprint(user)
    app.register_blueprint(authorization)

    return app
