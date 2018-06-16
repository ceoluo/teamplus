# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/1 10:55
# Author :  Richard
# File   :  views.py

from app import app
from flask import session, request, jsonify, g, redirect, url_for
from ..activity.forms import Activity
from app import models
# from .. import activity
import os
import time


ALLOWED_EXTENSIONS_FILE = ['doc','txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_FILE


file_path = 'no'


@app.route('/upload_activity_file', methods=['GET','POST'])
def upload_activity_file():
    if request.method == 'GET':
        return jsonify("请求错误")
    else:
        # db = models.Query()
        # last_id = db.get_last_aid()
        # print(last_id)
        # a_id = last_id + 1
        # a_id = 1095
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                # file.filename = 'file_' + str(a_id) + '.' + file.filename.rsplit('.')[1]
                file.filename = str(time.time()) +  '.' + file.filename.rsplit('.')[1]
                basepath = r"D:\\Python\\project\\team_plus\\app\\static\\file\\activity_file"
                upload_path = os.path.join(basepath, file.filename)
                path = r'../file/activity_file/' + file.filename
                global file_path
                file_path = path
                # Path().set_path(file_path)
                # print(Path().get_path())
                print(file_path)
                file.save(upload_path)
                # # 将图片路径更新到数据库
                # db = models.UpdateDB()
                # # path = r'..file/activity_file/'+ file.filename
                # db.update_activity_file(a_id, path)
                return redirect(url_for('static', filename='html/activity.html'))
        except Exception:
            return redirect(url_for('static', filename='html/activity.html'))


@app.route('/create_activity', methods=['GET', 'POST'])
def create_activity():
    u_id = session.get('u_id')
    # u_id = 29
    if request.method == 'GET' or u_id is None or u_id == '':
        return redirect(url_for('static', filename='index_html/index.html'))
    # print(request.form['a_name'])
    activity = Activity()
    # 从表单中获取到数据
    activity_data = activity.get_data(request)
    # 添加发起者信息
    print(activity_data)
    # 判断该活动是由个人还是团队创建
    # if activity_data['creator_level'] == 1:
    if activity_data['a_creator'] != 1:
        activity_data['creator_level'] = 1
        activity_data['a_imgs'] = file_path
        print(file_path)
        # 将数据插入数据库
        new_activity = models.InsertDB()
        a_id = new_activity.create_activity(activity_data)
        print("添加活动的状态：{}".format(a_id))
        if a_id != 0:
            # 将创建的活动添加到活动关联表中
            t_id = activity_data['a_creator']
            flag = models.InsertDB().join_activity_team(a_id, t_id)
            print(flag)
    else:
        print('file_path')
        print(file_path)
        print(file_path)
        activity_data['a_creator'] = u_id
        activity_data['a_imgs'] = file_path
        # 将数据插入数据库
        new_activity = models.InsertDB()
        a_id = new_activity.create_activity(activity_data)
        print("添加活动的状态：{}".format(a_id))
        if a_id != 0:
            # 将创建的活动添加到活动关联表中
            flag = models.InsertDB().join_activity(a_id, u_id)
            print(flag)
    return jsonify({'a_id': a_id})


@app.route('/get_activity_data',methods=['POST','GET'])
def get_activity_data():
    # 如果没登录就重定向
    u_id = session.get('u_id')
    # u_id = 29
    if u_id is None or u_id == '':
        return redirect(url_for('index'))
    data = {
        'code': 400,
        'data': {}
    }
    # 从数据库中查出指定id的活动
    a_id = int(request.args.get('a_id'))
    # a_id = 1000
    print(a_id)
    # a_id = 1000
    query = models.Query()
    activity_data = query.get_activity_data(a_id)
    member_count = query.activity_member_count(a_id)
    activity_data['member_count'] = member_count
    temp = []
    for x in query.get_joined_aid(u_id):
        temp.append(x[0])
    print(temp)
    if a_id in temp:
        activity_data['is_joined'] = 1
    else:
        activity_data['is_joined'] = 0
    data['code'] = 200
    data['data'] = activity_data
    return jsonify(data)


@app.route('/show_user_list')
def show_user_list():
    a_id = request.args.get('a_id')
    query = models.Query()
    user_list = query.show_user_list(a_id)
    print(user_list)
    return jsonify(user_list)


@app.route('/alter_activity')
def alter_activity():
    activity = Activity()
    new_activity_data = activity.get_data(request)
    # 将更新插入数据库
    a_id = g.a_id
    flag = models.UpdateDB().update_activity(a_id, new_activity_data)
    return jsonify(flag)


@app.route('/show_activities',methods=['GET'])
def show_activities():
    data = {
        'code': 400,
        'current_page': 1,
        'pages': 1,
        'data': [],
    }
    try:
        # 获取u_id
        # u_id = session.get('u_id')
        # u_id = 30
        # 获取活动的等级
        # a_level = 2
        a_level = request.args.get('a_level')
        print(a_level)
        query = models.Query()
        # 查出活动总数
        db_count = query.get_a_level_length(a_level)
        print(db_count)
        # 计算活动的页数
        pages = db_count//10 + 1
        data['pages'] = pages
        # 获取活动的页数
        current_page = int(request.args.get('current_page'))
        # current_page = 1
        start_id = (current_page-1)*8
        activities_data = query.get_level_activities(a_level, start_id)
        # if u_id is None or u_id == '':
        #     data['code'] = 400
        #     data['data'] = activities_data
        #     for x in activities_data:
        #         x['is_joined'] = 0
        #     return jsonify(data)
        print(activities_data)

        # 查出我已参加的活动,是一个tuple
        # joined_activities_id = query.get_joined_aid(u_id)
        # for x in activities_data:
        #     # 如果该活动我已参加，则标记True
        #     if x['a_id'] in joined_activities_id:
        #         x['is_joined'] = 1
        #     else:
        #         x['is_joined'] = 0
        #
        data['code'] = 200
        data['data'] = activities_data
    except Exception:
        return jsonify(data)
    finally:
        return jsonify(data)


# 展示已经参加了的活动
@app.route('/show_joined_activities')
def show_joined_activities():
    data = {
        'code': 400,
        'data': {}
    }
    u_id = session.get('u_id')
    # u_id = 29
    query = models.Query()
    joined_activities_data = query.get_joined_activities(u_id)
    data['code'] = 200
    data['data'] = joined_activities_data
    # print(joined_activities_data)
    return jsonify(data)


@app.route('/my_activity')
def my_activity():
    u_id = session.get('u_id')
    # u_id = 29
    query = models.Query()
    my_activity_id = query.get_my_aid(u_id)
    print(my_activity_id)
    return jsonify(my_activity_id)


# 参加活动
@app.route('/join_activity')
def join_activity():
    data = {
        'code': 400,
        'success': 0
    }
    u_id = session.get('u_id')
    # u_id = 29
    # if u_id is None or u_id == '':
    #     return redirect(url_for('index'))
    a_id = request.args.get('a_id')
    # a_id = 1000
    insert_activity = models.InsertDB()
    insert_activity.join_activity(u_id, a_id)
    data['code'] = 200
    data['success'] = 1
    return jsonify(data)


@app.route('/team_join_activity')
def team_join_activity():
    a_id = request.args.get('a_id')
    t_id = request.args.get('t_id')
    join_activity = models.InsertDB()
    res = join_activity.join_activity_team(a_id, t_id)
    print(res)
    return jsonify(res)
