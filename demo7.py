#-*- coding: UTF-8 -*-
import random

import requests
import time

ClickUrl='http://pv.open.com.cn/click.php?type=heatmap&clickTarget=1&logVisitId=676416e2-bbfe-420e-8161-d0e24de599c5-1480476177758&logBtsVal=676416e2-bbfe-420e-8161-d0e24de599c5&logUserid=huangbqopen&pageId=1480478024946-71835420633215114509135219839237&logUrl=%2Flearn.open.com.cn%2FStudentCenter%2FIndex&logcharset=UTF-8&logChannel=100200&logmx=185&logmy=364&ver=2015021001&time='
myRequests = requests.Session()
def click():
    print myRequests.get(ClickUrl+str("%d" %(time.time()*1000))).content


if __name__ == '__main__':
    while True:
        print time.strftime('%Y-%m-%d %X', time.localtime())
        t=random.randint(12, 20)
        print '稍等',t,'秒，再执行一下次'
        click()
        time.sleep(t)
