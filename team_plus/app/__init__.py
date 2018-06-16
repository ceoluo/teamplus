# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/4/25 13:12
# Author :  Richard
# File   :  __init__.py

from flask import Flask
from flask_cors import *

import config


app = Flask(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)

from app import models
# from app.user import forms, views
from app import user
# from app.activity import forms, views
from app import activity
# from app.team import forms, views
from app import team
from app import user_file
