# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/16 13:26
# Author :  Richard
# File   :  __init__.py

from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)

from app import jwc