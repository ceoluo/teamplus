# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/8 19:36
# Author :  Richard
# File   :  messages.py

import datetime

class Message(object):
    def __init__(self):
        self.m_id = 1
        self.u_id = 1
        self.m_content = ''
        self.m_date = ''
        self.be_m_id = 1
        self.be_m_level = 1

    def get_message_data(self, request):
        self.m_id = request.form['m_id']
        self.m_content = request.form['m_content']
        self.m_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.be_m_id = request.form['be_m_id']
        self.be_m_level = request.form['be_m_level']

