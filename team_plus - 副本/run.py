# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/4/29 11:21
# Author :  Richard
# File   :  run.py

from app import app


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=80, threaded=True)
