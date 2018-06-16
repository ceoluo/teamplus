# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/16 13:33
# Author :  Richard
# File   :  form.py

class FormData(object):
    def __init__(self):
        self.form_data = {
            'u_xh_id': '',
            'u_password':'',
            'check_code': ''
        }

    def get_data(self, request):
        self.form_data['u_xh_id'] = request.form['u_xh_id']
        self.form_data['u_password'] = request.form['u_password']
        self.form_data['check_code'] = request.form['check_code']
        return self.form_data