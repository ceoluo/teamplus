# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/16 13:25
# Author :  Richard
# File   :  run.py

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)