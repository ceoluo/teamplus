# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/8 19:36
# Author :  Richard
# File   :  views.py

from flask import session, request
from app import app
from app import models
from .messages import Message


@app.route('/send_message')
def send_message():
    # u_id = session.get('u_id')
    u_id = 29
    message = Message().get_message_data(request)
    # 插入数据库
    db = models.InsertDB()
    db.add_message(message)
    # 将留言与被流言方关联
    be_m_level = message['be_m_level']
    be_m_id = message['be_m_id']
    if be_m_level == 1:
        table_name = 'users'
        db.message_to_table(table_name, be_m_id,)


