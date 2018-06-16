# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/4/25 21:35
# Author :  Richard
# File   :  models.py

import pymysql
from config import DB_CONFIG


class Query(object):
    def get_u_id(self, u_xh_id):
        '''
        获取用户id
        :param u_xh_id:
        :return:
        '''
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select u_id from users WHERE u_xh_id='{}'".format(u_xh_id)
        # print(sql)
        sql = cursor.mogrify(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        db.close()
        if result:
            return result[0]['u_id']
        else:
            # print(False)
            return False

    def get_password(self, u_password):
        '''
        验证密码是否存在数据库
        :param u_password:
        :return:
        '''
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select u_id from users WHERE u_password='{}'".format(u_password)
        # print(sql)
        r_number = cursor.execute(sql)
        # print(r_number)
        db.close()
        if r_number == 0:
            return False
        else:
            return True

    def get_login_user(self, u_id):
        '''
        从数据库中查找出用户信息
        :param u_id:
        :return: 符合条件的用户信息 [{},]形式
        '''
        db = pymysql.connect(**DB_CONFIG)
        # 关于默认获取的数据是元祖类型，如果想要或者字典类型的数据:
        # 游标设置为字典类型
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select u_id,u_xh_id,u_nickname,head_img,u_introduction from users WHERE u_id={}".format(u_id)
        sql = cursor.mogrify(sql)
        cursor.execute(sql)
        results = cursor.fetchall()[0]
        # print(results)
        db.close()
        return results

    def get_user_data(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select u_id, u_xh_id,u_nickname,u_name,u_sex,u_race,u_birth," \
              "u_adm_time,u_add,u_introduction,u_title,u_faculty,u_discipline," \
              "head_img from users WHERE u_id={}".format(u_id)
        cursor.execute(sql)
        user_data = cursor.fetchall()[0]
        db.close()
        return user_data

    def get_activity_data(self, a_id):
        '''
        从数据库中查找指定id的活动的数据
        :param a_id:
        :return: activity_data
        '''
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select * from activities WHERE a_id={}".format(a_id)
        print(sql)
        cursor.execute(sql)
        activity_data = cursor.fetchall()[0]
        db.close()
        return activity_data

    def activity_member_count(self, a_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select count(*) from activity_user WHERE a_id={}".format(a_id)
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        return count

    def get_table_length(self,table_name=''):
        '''
        查询指定表的记录条数
        :param table_name:
        :return: int
        '''
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select count(*) from {}".format(table_name)
        cursor.execute(sql)
        count = cursor.fetchone()
        return count[0]

    def get_a_level_length(self, level, table_name='activities'):
        '''
        获取指定等级活动的记录数
        :param level:
        :return:
        '''
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select count(*) from {} WHERE a_level={}".format(table_name,level)
        print(sql)
        cursor.execute(sql)
        count = cursor.fetchone()
        db.close()
        return count[0]

    def get_level_activities(self, a_level,start_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        # sql = "select * from activities WHERE a_level= {}".format(a_level)
        sql = "SELECT a_id,a_name,a_imgs,a_level,a_introduction,a_begin_time,a_end_time,a_creator " \
              "FROM activities WHERE a_level={} " \
              "and a_id >= (SELECT a_id FROM activities LIMIT {}, {}) " \
              "LIMIT 8;".format(a_level, start_id, start_id+1)
        print(sql)
        cursor.execute(sql)
        activities = cursor.fetchall()
        db.close()
        return activities

    def get_my_aid(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select a_id,a_name,a_imgs,a_introduction,a_begin_time,a_end_time " \
              "from activities WHERE creator_level=2 and a_creator={}".format(u_id)
        print(sql)
        cursor.execute(sql)
        my_aid = cursor.fetchall()
        db.close()
        return my_aid

    def get_joined_aid(self,u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select a_id  from activity_user WHERE u_id= {}".format(u_id)
        print(sql)
        cursor.execute(sql)
        joined_activities_data = cursor.fetchall()
        print(joined_activities_data)
        db.close()
        return joined_activities_data

    def get_joined_activities(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select *  from activities join activity_user " \
              "WHERE activity_user.u_id={} " \
              "and activities.a_id=activity_user.a_id".format(u_id)
        print(sql)
        cursor.execute(sql)
        joined_activities_data = cursor.fetchall()
        db.close()
        return joined_activities_data

    def show_user_list(self, a_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select users.u_id,u_nickname,head_img from users join activity_user " \
              "on users.u_id=activity_user.u_id WHERE a_id={}".format(a_id)
        print(sql)
        cursor.execute(sql)
        user_list = cursor.fetchall()
        return user_list

    def get_last_aid(self):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select max(a_id) from activities;"
        cursor.execute(sql)
        last_id = cursor.fetchone()[0]
        db.close()
        return last_id

    def show_joined_tid(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select t_id from team_user WHERE u_id={}".format(u_id)
        cursor.execute(sql)
        joined_data = cursor.fetchone()
        db.close()
        return joined_data

    def get_my_teams(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select teams.t_id,t_name,t_introduction,t_imgs " \
              "from teams join administrator on teams.t_id=administrator.t_id " \
              "WHERE administrator.u_id={} ".format(u_id)
        print(sql)
        cursor.execute(sql)
        my_tid = cursor.fetchall()
        db.close()
        return my_tid

    def get_my_tid(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select teams.t_id,t_name from teams join administrator " \
              "on teams.t_id=administrator.t_id " \
              "WHERE administrator.u_id={}".format(u_id)
        print(sql)
        cursor.execute(sql)
        my_tid = cursor.fetchall()
        db.close()
        # print(my_tid)
        return my_tid

    def show_joined_teams(self, u_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select *  from teams join team_user " \
              "WHERE team_user.u_id={} " \
              "and teams.t_id=team_user.t_id".format(u_id)
        print(sql)
        cursor.execute(sql)
        joined_data = cursor.fetchall()
        db.close()
        return joined_data

    def get_team_data(self, t_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select * from teams WHERE t_id={}".format(t_id)
        print(sql)
        cursor.execute(sql)
        team_data = cursor.fetchall()[0]
        db.close()
        return team_data

    def count_joined_members(self, t_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select count(*) from team_user WHERE t_id={}".format(t_id)
        print(sql)
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        db.close()
        return count

    def show_teams(self, t_level, start_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "SELECT * FROM teams " \
              "WHERE t_level={} and t_id >= (SELECT t_id FROM activities LIMIT {}, {}) " \
              "LIMIT 8".format(t_level, start_id, start_id+1)
        print(sql)
        cursor.execute(sql)
        team_data = cursor.fetchall()
        db.close()
        return team_data

    def get_team_members(self, t_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select u_id from team_user WHERE t_id={}".format(t_id)
        cursor.execute(sql)
        res = cursor.fetchall()
        db.close()
        return res

    def get_teams_length(self, t_level=3):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "select count(*) from teams WHERE t_level={}".format(t_level)
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        db.close()
        return count

class InsertDB(object):
    def __init__(self):
        self.a_id = 3

    def add_user(self, object, u_password):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()

        sql = "insert into users (u_xh_id,u_name,u_nickname,u_password,u_sex," \
              "u_race,u_birth,u_adm_time,u_add,head_img,u_introduction,u_title," \
              "u_faculty,u_discipline) " \
              "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(object['学号'],
               object['姓名'], object['学号'], u_password, object['性别'], object['民族'], object['出生日期'],
               object['入学日期'][:4]+"-"+object['入学日期'][4:6]+"-"+object['入学日期'][6:8],
               object['籍贯'].replace('\n', ''), "head_img.jpg", "生活不止眼前的诗和田野...", "校园小白", object['学院'],
               object['专业方向'])
        try:
            # print(sql)
            cursor.execute(sql)
            db.commit()
            print("提交了insert")
        except Exception as e:
            db.rollback()
            print("insert 失败")
        finally:
            db.close()
            print("insert success")

    def join_class_team(self, u_id, u_data):
        '''
        新用户加入班级
        传参：爬取到的信息u_data
        :return:
        '''
        class_name = u_data['行政班']
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        # 查询该团队是否存在于teams表中
        sql = "select t_id from teams where t_name='{}'".format(class_name)
        r_number = cursor.execute(sql)
        cursor.close()
        # 如果不存在，则添加团队
        try:
            if r_number == 0:
                cursor = db.cursor()
                sql = "insert into teams (t_name) VALUES ('{}')".format(class_name)
                cursor.execute(sql)
                cursor.close()
                db.commit()
            # 将team和user关联到team_user表中
            # 1.检查t_id存在性
            cursor = db.cursor()
            sql = "select t_id from teams where t_name='{}'".format(class_name)
            cursor.execute(sql)
            t_id = cursor.fetchall()
            # print(t_id)
            # t_id = ((2001,),)
            t_id = t_id[0][0]
            cursor.close()
            # 2.添加关联
            cursor = db.cursor()
            sql = "insert into team_user (t_id,u_id) VALUES ({},{})".format(t_id, u_id)
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
        finally:
            db.close()

    def create_activity(self, activity_data):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        # print(activity_data)
        sql = "insert into activities (a_name,a_introduction,a_begin_time," \
              "a_end_time,a_level,a_imgs,a_file,a_creator,creator_level,a_content) " \
              "VALUES ('{}','{}','{}','{}',{},'{}','{}',{}," \
              "{},'{}')".format(activity_data['a_name'],
                                activity_data['a_introduction'],
                                activity_data['a_begin_time'],
                                activity_data['a_end_time'],
                                activity_data['a_level'],
                                activity_data['a_imgs'],
                                activity_data['a_file'],
                                activity_data['a_creator'],
                                activity_data['creator_level'],
                                activity_data['a_content'])
        sql = cursor.mogrify(sql)
        print(sql)
        try:
            cursor.execute(sql)
            self.a_id = cursor.lastrowid
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return self.a_id

    def join_activity(self, u_id, a_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "insert into activity_user (u_id,a_id) VALUES ({},{})".format(u_id, a_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return False
        finally:
            db.close()
            return True

    def create_team(self,team_data):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "insert into teams (t_name,t_introduction,t_level,t_imgs,t_file,t_members) " \
              "VALUES ('{}','{}',{},'{}','{}',{})".format(team_data['t_name'],
                                                       team_data['t_introduction'],
                                                       team_data['t_level'],
                                                       team_data['t_imgs'],
                                                       team_data['t_file'],
                                                       team_data['t_members'])
        t_id = 0
        print(sql)
        try:
            # print(sql)
            cursor.execute(sql)
            t_id = cursor.lastrowid
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return t_id

    def join_team_admin(self, u_id, t_id, ad_level=1):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "INSERT into administrator (t_id,u_id,ad_level) VALUE ({},{},{})".format(t_id,u_id,ad_level)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1

    def join_team(self, u_id, t_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "insert into team_user (t_id,u_id) VALUES ({},{})".format(t_id,u_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            cursor.close()
            return 1
        except Exception:
            print("Error")
            db.rollback()
            return 0

    def join_activity_team(self,a_id, t_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = 'insert into activity_team (a_id,t_id) VALUES ({},{})'.format(a_id, t_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1

    def add_message(self, message):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "insert into messages (u_id,m_content,m_date) " \
              "VALUES ({},'{}','{}')".format(message['u_id'],message['m_content'],message['m_data'])
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1

    def message_to_table(self, table_name, u_id, m_id):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "insert into {} (u_id,m_id) " \
              "VALUES ({},{})".format(table_name,u_id,m_id)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1


class UpdateDB(object):
    def update_user(self, u_id, new_data):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "update users set u_nickname='{}',u_add='{}'," \
              "u_introduction='{}',u_title='{}'" \
              "WHERE u_id={}".format(new_data['u_nickname'],
                                     new_data['u_add'],
                                     new_data['u_introduction'],
                                     new_data['u_title'],
                                     u_id)
        try:
            print(sql)
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1

    def update_activity(self, a_id, new_activity_data):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "update activities " \
              "set a_name='{}',a_introduction='{}',a_begin_time='{}'," \
              "a_end_time='{}',a_level='{}',a_imgs='{}',a_file='{}'" \
              "WHERE a_id={}".format(new_activity_data['a_name'],new_activity_data['a_introduction'],
                                     new_activity_data['a_begin_time'],new_activity_data['a_end_time'],
                                     new_activity_data['a_level'],new_activity_data['a_imgs'],
                                     new_activity_data['a_file'],a_id)
        cursor.mogrify(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return

    def update_head_img(self, u_id, path):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "update users set head_img='{}' WHERE u_id={}".format(path, u_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1

    def update_activity_file(self, a_id, path):
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "update activities set a_imgs='{}' WHERE a_id={}".format(path, a_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            return 0
        finally:
            db.close()
            return 1
