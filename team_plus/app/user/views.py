# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/4/25 13:16
# Author :  Richard
# File   :  views.py

from flask import jsonify, request, url_for, redirect, session, g, make_response

from app import app, models
from app.user import forms
from app.user.scraping import Scraping


@app.route('/')
def index():
    u_id = session.get('u_id')
    if u_id is None or u_id == '':
        return redirect(url_for('static', filename='html/index.html'))
    else:
        return redirect(url_for('static', filename='html/index.html'))


@app.route('/check_login')
def check_login():
    data = {
        'is_login': 0
    }
    u_id = session.get('u_id')
    if u_id is None or u_id == '':
        return jsonify(data)
    else:
        data['is_login'] = 1
        return jsonify(data)


scraping = Scraping()


@app.route('/check_code')
def check_code():
    if session.get('u_id') is None or session.get('u_id') == '':
        scraping.crow_check_code()
    return app.send_static_file('check_code.jpg')
    # return redirect(url_for('static', filename='static/check_code.jpg'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    # login = models.Login()
    # 实例化login_form类用于获取登录表单信息
    # print(session['u_id'])
    # try:
    #     if session['u_id'] is None or session['u_id'] == '':
    #         return redirect(url_for('static', filename='html/index.html'))
    # except Exception:
    #     return redirect(url_for('static', filename='html/index.html'))
    # finally:
    #     pass
    login_form = forms.LoginForm()
    form_data = login_form.get_data(request)
    print(form_data)
    db_select = models.Query()
    # 检查数据库中有没有个人信息
    # 在数据库中获取u_id
    u_id = db_select.get_u_id(form_data['u_xh_id'])
    print(u_id)
    u_xh_id = form_data['u_xh_id']
    u_password = form_data['u_password']
    data = {
        'code': 400,
        'data': {}
    }
    if u_id and db_select.get_password(u_password):
        # 登录成功，建立对话
        session['u_id'] = u_id
        session['u_xh_id'] = u_xh_id
        session['u_password'] = u_password
        # g.u_id = u_id
        u_data = db_select.get_login_user(u_id)
        data['code'] = 200
        data['data'] = u_data
        print('login success!')
        # print(data)
        # 登录成功重定向到首页
        return jsonify(data)
    # 爬取数据
    try:
        # 爬取到用户的个人信息
        u_data = scraping.crow_date(form_data)
    except Exception:
        return jsonify(data)
    else:
        # 爬取成功，插入数据库
        db_insert = models.InsertDB()
        db_insert.add_user(u_data, u_password)
        print("插入成功!")
        print(u_data)
        # 向teams和team_user插入数据
        u_id = db_select.get_u_id(u_xh_id)
        db_insert.join_class_team(u_id, u_data)
        session['u_id'] = u_id
        session['u_xh_id'] = u_xh_id
        session['u_password'] = u_password
        g.u_id= u_id
        u_data = db_select.get_login_user(u_id)
        data['code'] = 200
        data['data'] = u_data
        return jsonify(data)


@app.route('/my_data')
def my_data():
    data = {
        'code': 400,
        'data': {}
    }
    query = models.Query()
    u_id = session.get('u_id')
    # u_id = 29
    print(u_id)
    print(request.cookies)
    if u_id is None:
        return jsonify(request.cookies)
    u_data = query.get_user_data(u_id)
    data['code'] = 200
    data['data'] = u_data
    print(data)
    # resp = make_response(jsonify(response=data))
    # # 跨域设置
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Access-Control-Allow-Credentials'] = 'true'
    # resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # resp.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    return jsonify(data)


@app.route('/alter_my_data',methods=['GET', 'POST'])
def alter_user_data():
    if request.method == 'GET':
        return redirect(url_for('static', filename='html/index.html'))
    else:
        data = {
            'data': 0
        }
        alter_form = forms.User()
        # 从表单中获取数据
        alter_data = alter_form.get_data(request)
        # 将改变的数据更新到数据库
        u_id = session.get('u_id')
        # u_id = 29
        update_db = models.UpdateDB()
        update = update_db.update_user(u_id,alter_data)
        print("个人信息修改：".format(update))
        data['data'] = 1
        return jsonify(data)

