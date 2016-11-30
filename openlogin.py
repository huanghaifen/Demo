#! /usr/bin/env python
# coding:utf-8

import sys
import re
import urllib2
import urllib
import requests
import cookielib
import time
#-*- coding: UTF-8 -*-
import pytesseract
from PIL import Image

## 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")
#####################################################
# 登录
loginurl = 'http://learn.open.com.cn/share/left?bust=1480382872644&_=1480382872646'
logindomain = 'open.com.cn'


class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, username, password, domain):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.domain = domain

    def login(self):
        '''登录网站'''
        #注意一下如果是aspx的请求，要加上一些奇怪的请求头。
        #loginparams = {'wp-submit': '登录', 'pwd': 'fen880810','log':'hvaning','redirect_to':'http://www.iyunying.org/wp-admin/','testcookie':'1'}
        loginparams={}
        headers = {
       'Accept':'application / json, text / javascript, * / *; q = 0.01',
       # 'Accept - Encoding':'gzip, deflate, sdch',
      'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
        'Cookie':'b_t_s_100200=28f01bcf-9be9-4151-87bc-46d01e6bc07c; up_first_date=2016-10-31; b_t_s_100100=6ea92eed-78bd-4832-8be2-a61382506cca; up_beacon_id_100200=28f01bcf-9be9-4151-87bc-46d01e6bc07c-1480379130143; ASP.NET_SessionId=wh5ykxyp53fdva3kfzokkmdv; up_page_stime_100200=1480381192618; up_beacon_vist_count_100200=2; up_page_stime_100100=1480381267180; up_beacon_vist_count_100100=1; up_beacon_id_100100=6ea92eed-78bd-4832-8be2-a61382506cca-1480381267184; Hm_lvt_946766664d58c814a94301842a7a73fb=1477980324,1480381267; Hm_lpvt_946766664d58c814a94301842a7a73fb=1480381267; LmsForm=Name=huangbqopen&Pwd=open1609&RememberMe=1; up_beacon_user_id_100200=huangbqopen; Hm_lvt_686401bd1a1f7184252b460af0f4337e=1479947104,1480033331,1480292754,1480379130; Hm_lpvt_686401bd1a1f7184252b460af0f4337e=1480382872; up_beacon_uni_id_100200=10027',
        'Host':'learn.open.com.cn',
        'Referer':'http: // learn.open.com.cn / StudentCenter / Index'
        #'X - Requested - With':'XMLHttpRequest'
        }

        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        url=self.operate.geturl()
        print url
        thePage = response.read()
        print thePage

if __name__ == '__main__':
    userlogin = Login()
    username = 'huanghaifen'
    password = '329481'
    domain = logindomain
    i = 0;
    while True:
        print time.strftime('%Y-%m-%d %X', time.localtime())
        i += 1
        userlogin.setLoginInfo(username, password, domain)
        userlogin.login()
        time.sleep(300)




