# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/4/25 21:36
# Author :  Richard
# File   :  forms.py

class User(object):
    def __init__(self):
        self.user_data = {
            'u_nickname': '',
            'u_add': '',
            'u_title': '',
            'u_introduction': '',
            'head_img': '',
        }

    def get_data(self, request):
        self.user_data['u_nickname'] = request.form['u_nickname']
        self.user_data['u_add'] = request.form['u_add']
        self.user_data['u_title'] = request.form['u_title']
        self.user_data['u_introduction'] = request.form['u_introduction']
        self.user_data['head_img'] = request.form['head_img']
        return self.user_data


class LoginForm(object):
    def __init__(self):
        self.form_data = {
            'u_xh_id': '',
            'u_password': '',
            'check_code': ''
        }

    def get_data(self, object):
        self.form_data['u_xh_id'] = object.form.get('u_xh_id')
        self.form_data['u_password'] = object.form.get('u_password')
        self.form_data['check_code'] = object.form.get('check_code')
        return self.form_data

