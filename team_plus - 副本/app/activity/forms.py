# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/1 10:55
# Author :  Richard
# File   :  forms.py


class Activity(object):
    def __init__(self):
        print()
        self.activity_data = {
            'a_name': '',
            'a_introduction': '',
            'a_begin_time': '',
            'a_end_time': '',
            'a_level': 3,
            'a_imgs': 'no',
            'a_file': 'no',
            'a_creator': 0,
            'creator_level': 2,
            'a_content': ''
        }

    def get_data(self, request):
        self.activity_data['a_name'] = request.form['a_name']
        self.activity_data['a_introduction'] = request.form['a_introduction']
        self.activity_data['a_begin_time'] = request.form['a_begin_time']
        self.activity_data['a_end_time'] = request.form['a_end_time']
        self.activity_data['a_level'] = request.form['a_level']
        # self.activity_data['a_imgs'] = Path().get_path()
        self.activity_data['a_creator'] = int(request.form['a_creator'])
        self.activity_data['a_content'] = request.form['a_content']
        # print(Path().get_path())
        return self.activity_data