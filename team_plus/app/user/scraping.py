# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/4/27 8:46
# Author :  Richard
# File   :  scraping.py

import requests
from bs4 import BeautifulSoup
import re
from urllib import parse


class Scraping(object):

    def __init__(self, url='http://jwc.xhu.edu.cn/'):
        self.url = url
        # 建立对话
        self.session = requests.session()
        self.__VIEWSTATE = ''
        self.index_response = b''

    # 爬取到首页
    def crow_check_code(self):
        r = self.session.get(self.url)
        # print(r.headers['set-cookie'])
        soup = BeautifulSoup(r.content, 'html.parser')
        # 解析出__VIEWSTATE
        self.__VIEWSTATE = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
        # print(self.__VIEWSTATE)

        # print(r.headers['set-cookie'])
        # cookie_split = str(r.headers['set-cookie']).split(',')
        # cookie = cookie_split[0].split(' path=/')[0] + cookie_split[1].split('; path=/')[0]

        ck_url = 'http://jwc.xhu.edu.cn/CheckCode.aspx'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'Host': 'jwc.xhu.edu.cn',
            'Referer': 'http://jwc.xhu.edu.cn/default2.aspx',
            'Connection': 'keep - alive',
            # 'Cookie': cookie
        }
        ck_code = self.session.get(ck_url, headers=headers)
        # 下载验证码
        with open('D:\\Python\project\\team_plus\\app\static\\check_code.jpg', 'wb') as check_code:
            check_code.write(ck_code.content)
            check_code.close()
        return True

    def crow_index(self, login_data):
        headers = {
            'Accept': 'text/index_html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': cookie,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'jwc.xhu.edu.cn',
            'Origin': 'http://jwc.xhu.edu.cn',
            'Referer': 'http://jwc.xhu.edu.cn/default2.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        # check_code_img = input("请输入验证码：")
        post_data = {
            '__VIEWSTATE': self.__VIEWSTATE,
            'txtUserName': login_data['u_xh_id'],
            'TextBox2': login_data['u_password'],
            'txtSecretCode': login_data['check_code'],
            'RadioButtonList1': '学生'.encode('gb2312'),
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': '',
        }
        self.index_response = self.session.post("http://jwc.xhu.edu.cn/default2.aspx",
                                                data=post_data, headers=headers).content
        # print(response.content.decode('gb2312'))
        return self.index_response

    # 在首页中获取数据
    def crow_name(self):
        soup = BeautifulSoup(self.index_response.decode('gb2312'), 'html.parser')
        xhxm_span = soup.find('span', attrs={'id': 'xhxm'})
        # print(xhxm)
        p = re.compile('<[^>]+>')
        xhxm_span = str(xhxm_span)
        xhxm = p.sub("", xhxm_span).replace('同学', '')
        return xhxm

    def crow_date(self, login_data):
        self.crow_index(login_data)
        # index_url = 'http://jwc.xhu.edu.cn/xs_main.aspx?xh=3120160911123'
        u_xh_id = login_data['u_xh_id']
        data = {
            'gnmkdm': 'N121501',
            'xh': u_xh_id,
            # 'xm': self.crow_name(login_data).encode('gb2312')
            # 将姓名转化为url格式的编码
            'xm':  parse.quote(self.crow_name().encode('gb2312'))
        }
        index_url = "http://jwc.xhu.edu.cn/xsgrxx.aspx?xh={xh}&xm={xm}&gnmkdm={gnmkdm}".format(**data)
        # print(index_url)
        headers = {
            'Accept': 'text/index_html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': cookie,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'jwc.xhu.edu.cn',
            'Origin': 'http://jwc.xhu.edu.cn',
            'Referer': 'http://jwc.xhu.edu.cn/default2.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        user_date = self.session.get(index_url, headers=headers)
        # print(user_date.status_code)
        user_date_html = user_date.content.decode('gb2312')
        soup = BeautifulSoup(user_date_html, 'html.parser')
        user_date_list = soup.find_all('td')
        user_date_list.pop(6)
        # print(user_date_list)
        user_date_dict = {}
        p = re.compile('<[^>]+>')
        for i in range(0, len(user_date_list)-1):
            td_data_key = str(user_date_list[i])
            td_data_value = str(user_date_list[i+1])
            td_data_key = p.sub("", td_data_key).split('：')[0]
            td_data_value = p.sub("", td_data_value)
            if i % 2 == 0:
                user_date_dict[td_data_key] = td_data_value
        return user_date_dict


if __name__ == '__main__':
    url = 'http://jwc.xhu.edu.cn/'
    # user_id = input("学号：")
    # password = input("密码：")
    login_data = {
        'u_id': '3120160911123',
        'u_password': 'lx201091',
        'check_code': ''
    }
    scraping = Scraping(url)
    check_code = scraping.crow_check_code()
    login_data['check_code'] = input("yzm:")
    # print(check_code)
    # user_name = scraping.crow_index(check_code)
    # user_name = scraping.crow_name()

    crow_data = scraping.crow_date(login_data)
    print(crow_data)
