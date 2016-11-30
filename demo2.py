#-*- coding: UTF-8 -*-
import time
import urllib2


def task(i):
    urlstr='http://learn.open.com.cn/Common/Statistics/UserRequestLogBegin?UserName=huangbqopen&UserType=student&CurrentPage=%2fStudentCenter%2fIndex'
    html = urllib2.urlopen(urlstr,timeout=30).read()
    # -*- coding: UTF-8 -*-
    print '第',str(i),'次'
    #print html.decode("gbk").encode("utf-8")

def tasking(j):
    urlstr='http://pv.open.com.cn/info.php?logChannel=100200&logVisitId=28f01bcf-9be9-4151-87bc-46d01e6bc07c-1480379130143&logBtsVal=28f01bcf-9be9-4151-87bc-46d01e6bc07c&logUserid=huangbqopen&logOsType=chrome/54.0.2840.59&logdetectOS=other&logUrl=%2flearn.open.com.cn%2fstudentcenter%2findex&logHisRefer=-&logkw=-&logQuery=pageId=1480382872596-13197459352433758557816455094714&title=%E5%AD%A6%E7%94%9F%E4%B8%AD%E5%BF%83-%E5%A5%A5%E9%B9%8F%E5%AD%A6%E7%94%9F%E5%B9%B3%E5%8F%B0&charset=UTF-8&sr=1920*1080&logFirstdate=2016-10-31&loguni=10027&ver=2015021001&time=1480382872602'
    html = urllib2.urlopen(urlstr,timeout=30).read()
    # -*- coding: UTF-8 -*-
    print '第',str(j),'次'
    #print html.decode("gbk").encode("utf-8")


def timer(n):
    i=0;
    j=0;
    while True:
        print time.strftime('%Y-%m-%d %X', time.localtime())
        i+=1
        j+=1
        task(i)
        tasking(j)
        time.sleep(n)


if __name__ == '__main__':
    timer(300)