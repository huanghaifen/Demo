#! /usr/bin/env python
# coding:utf-8

import sys
import re
import urllib2
import urllib
import requests
import cookielib
from xtls.util import BeautifulSoup

## 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")
#####################################################
# 登录
loginurl = 'http://www.iyunying.org/wp-login.php'
logindomain = 'iyunying.org'


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
        loginparams = {'wp-submit': '登录', 'pwd': 'fen880810','log':'hvaning','redirect_to':'http://www.iyunying.org/wp-admin/','testcookie':'1'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36'
            ,'Cookie':'nvyj_2132_saltkey=S2n92244; nvyj_2132_lastvisit=1479103010; wp-settings-296=mfold%3Df; wp-settings-time-296=1479112080; WP-LastViewedPosts=a%3A5%3A%7Bi%3A0%3Bi%3A78554%3Bi%3A1%3Bi%3A78543%3Bi%3A2%3Bi%3A78324%3Bi%3A3%3Bi%3A77893%3Bi%3A4%3Bi%3A78723%3B%7D; nvyj_2132_lastact=1480323749%09api.php%09js; Hm_lvt_63807980f199e631f305b5f708985ca2=1479106614,1480323756; Hm_lpvt_63807980f199e631f305b5f708985ca2=1480323756; wordpress_logged_in_0f132dbc9344d2831f2ea7949fd1908c=hvaning%7C1480496637%7CBeBDMiX8oepi8quCIsXY6NJ5vVmjNByVl6ilxR3CKsd%7C65aed17b626bc9857eb8bec61f27f412e4e0bf4992eb00934bf5864a39c5bbde; wordpress_test_cookie=WP+Cookie+check'
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
    userlogin.setLoginInfo(username, password, domain)
    userlogin.login()