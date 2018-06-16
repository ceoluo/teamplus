# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/4 12:18
# Author :  Richard
# File   :  forms.py


class Team(object):
    def __init__(self):
        self.team_data = {
            't_name': '',
            't_introduction': '',
            't_imgs': 'hhh',
            't_file': 'fff',
            't_level': 3,
            't_members': 0
        }

    def get_team_data(self, request):
        print(request.form['t_name'])
        self.team_data['t_name'] = request.form['t_name']
        # print(self.team_data['t_name'])
        self.team_data['t_introduction'] = request.form['t_introduction']
        # self.team_data['t_imgs'] = request.form['t_imgs']
        self.team_data['t_level'] = request.form['t_level']
        # self.team_data['t_file'] = request.form['t_file']
        self.team_data['t_members'] = request.form['t_members']
        # print(self.team_data)
        return self.team_data




