# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/4 12:19
# Author :  Richard
# File   :  views.py

from app import app
from .. import models
from .forms import Team
from flask import session, request, jsonify, redirect, url_for
from  ..activity.forms import Activity


# @app.route('/test')
# def test():
#     return 'test'


@app.route('/create_team', methods=['GET', 'POST'])
def create_team():
    data = {
        'code': 400,
        't_id': 0
    }
    if request.method == 'GET':
        return redirect(url_for('index'))
    u_id = session.get('u_id')
    # u_id = 29
    try:
        team = Team()
        print(request.form.get('t_name'))
        team_data = team.get_team_data(request)
        print(team_data)
        # 将数据插入数据库
        db = models.InsertDB()
        t_id = db.create_team(team_data)
        print(t_id)
        # 将团队的创建者与管理员表与组成表关联起来
        db.join_team_admin(u_id, t_id)
        db.join_team(u_id, t_id)
        data['code'] = 200
        data['t_id'] = t_id
    except Exception:
        return jsonify(data)
    finally:
        return jsonify(data)


@app.route('/join_team')
def join_team():
    data = {
        'code': 400,
        'data': {}
    }
    try:
        u_id = session.get('u_id')
        # print(u_id)
        # u_id = 29
        t_id = request.args.get('t_id')
        print(t_id)
        # t_id = 1000
        db = models.InsertDB()
        temp = db.join_team(u_id, t_id)
        print(temp)
        data['code'] = 200
        data['data']['is_joined'] = temp
    except Exception:
        return jsonify(data)
    return jsonify(data)


@app.route('/my_teams')
def my_teams():
    u_id = session.get('u_id')
    # u_id = 29
    query = models.Query()
    my_teams_data = query.get_my_teams(u_id)
    return jsonify(my_teams_data)


@app.route('/my_teams_id')
def my_teams_id():
    u_id = session.get('u_id')
    # u_id = 29
    query = models.Query()
    my_teams_id = query.get_my_tid(u_id)
    return jsonify(my_teams_id)


@app.route('/show_joined_teams')
def show_joined_teams():
    data = {
        'code': 400,
        'data': {}
    }
    try:
        u_id = session.get('u_id')
        # u_id = 29
        query = models.Query()
        show_joined_teams = query.show_joined_teams(u_id)
        data['code'] = 200
        data['data'] = show_joined_teams
        return jsonify(data)
    except Exception:
        return jsonify(data)


@app.route('/show_team_data')
def show_team_data():
    data = {
        'code': 400,
        'data': {}
    }
    # session['u_id'] = 29
    try:
        u_id = session.get('u_id')
        if u_id is None or u_id == '':
            data['data']['login'] = "Please login！"
            return jsonify(data)
        # u_id = 29
        t_id = request.args.get('t_id')
        query = models.Query()
        team_data = query.get_team_data(t_id)
        # print(team_data)
        count_joined_members = query.count_joined_members(t_id)
        # print(count_joined_members)
        joined_team_tid = query.show_joined_tid(u_id)
        # print(t_id)
        # print(joined_team_tid)
        if int(t_id) in joined_team_tid:
            # print(team_data)
            team_data['is_joined'] = 1
        else:
            team_data['is_joined'] = 0
        data['code'] = 200
        data['data'] = team_data
        data['data']['count_joined_members'] = count_joined_members
    except Exception:
        print('Error')
        return jsonify(data)
    return jsonify(data)


@app.route('/show_teams')
def show_teams():
    data = {
        'code': 400,
        'current_page': 1,
        'data': {}
    }
    query = models.Query()
    t_level = request.args.get('t_level')
    db_count = query.get_teams_length(t_level)
    print(db_count)
    # 计算活动的页数
    pages = db_count // 10 + 1
    data['pages'] = pages
    current_page = int(request.args.get('current_page'))
    print(current_page)
    start_id = (current_page - 1) * 8
    teams_data = query.show_teams(t_level, start_id)
    data['code'] = 200
    data['data'] = teams_data
    data['current_page'] = current_page
    return jsonify(data)


@app.route('/show_members')
def show_members():
    t_id = request.args.get('t_id')
    query = models.Query()
    res = query.get_team_members(t_id)
    print(res)
    return jsonify(res)


# @app.route('/show_')