# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/5/12 13:13
# Author :  Richard
# File   :  user_file.py

from app import app
from flask import request, jsonify, session, redirect, url_for
import os
from app import models
import time

ALLOWED_EXTENSIONS_HEAD = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_EXTENSIONS_FILE = ['doc','txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

# class Path(object):
#     def __init__(self):
#         self.file_path = ''
#
#     def set_path(self, file_path):
#         self.file_path = file_path
#
#     def get_path(self):
#         return self.file_path


def allowed_img(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS_HEAD


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_FILE


@app.route('/upload_img', methods=['GET','POST'])
def upload_img():
    if request.method == 'GET':
        return jsonify("请求错误")
    else:
        session['u_id'] = 29
        u_id = session['u_id']
        try:
            file = request.files['file']
            if file and allowed_img(file.filename):
                # file.filename = 'head_img_' + str(session.get('u_id')) + '.' + file.filename.rsplit('.')[1]
                file.filename = str(time.time()).replace('.', '') + '.' + file.filename.rsplit('.')[1]
                basepath = r"D:\\Python\\project\\team_plus\\app\\static\\file\\head_img"
                upload_path = os.path.join(basepath, file.filename)
                file.save(upload_path)
                # 将图片路径更新到数据库
                db = models.UpdateDB()
                path = r'../file/head_img/' + file.filename
                db.update_head_img(u_id,path)
                # print(flag)
                return redirect(url_for('static',filename='html/activity.html'))
        except Exception:
            return redirect(url_for('static',filename='html/activity.html'))


# @app.route('/upload_activity_file', methods=['GET','POST'])
# def upload_activity_file():
#     if request.method == 'GET':
#         return jsonify("请求错误")
#     else:
#         db = models.Query()
#         last_id = db.get_last_aid()
#         # print(last_id)
#         a_id = last_id + 1
#         try:
#             file = request.files['file']
#             if file and allowed_img(file.filename):
#                 file.filename = 'file_' + str(a_id) + '.' + file.filename.rsplit('.')[1]
#                 basepath = r"D:\\Python\\project\\team_plus\\app\\static\\file\\activity_file"
#                 upload_path = os.path.join(basepath, file.filename)
#                 path = r'..file/activity_file/' + file.filename
#                 # file_path = path
#                 # Path().set_path(file_path)
#                 # print(Path().get_path())
#                 print(path)
#                 file.save(upload_path)
#                 # 将图片路径更新到数据库
#                 db = models.UpdateDB()
#                 # path = r'..file/activity_file/'+ file.filename
#                 db.update_activity_file(a_id, path)
#                 return redirect(url_for('static', filename='html/activity.html'))
#         except Exception:
#             return redirect(url_for('static', filename='html/activity.html'))


@app.route('/upload_team_file', methods=['GET','POST'])
def upload_team_file():
    if request.method == 'GET':
        return jsonify("请求错误")
    else:
        db = models.Query()
        last_id = db.get_last_aid()
        # print(last_id)
        a_id = last_id + 1
        try:
            file = request.files['file']
            if file and allowed_img(file.filename):
                file.filename = 'file_' + str(a_id) + '.' + file.filename.rsplit('.')[1]
                basepath = r"D:\\Python\\project\\team_plus\\app\\static\\file\\activity_file"
                upload_path = os.path.join(basepath, file.filename)
                global FILE_PATH
                FILE_PATH = upload_path
                file.save(upload_path)
                return jsonify({'data': 'success'})
        except Exception:
            return jsonify({'data': '请选择正确格式的图片！'})
