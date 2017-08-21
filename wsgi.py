#!usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
