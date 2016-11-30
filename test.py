import os

import requests
from PIL import Image

URL1 = 'http://learn.open.com.cn/Account/ValidatePic?0.11095544709118756'
URL2 = 'http://learn.open.com.cn/Account/UnitLogin?t=134&loginName=huangbqopen&passWord=open1609&rememberMe=1&validatenum='
CodesImg = os.path.join(os.getcwd(), 'imgcode.jpg')
session = requests.Session()

r = session.get(URL1)
f = open(CodesImg, 'wb')
f.write(r.content)
f.close()
im = Image.open('imgcode.jpg')
im.show()
code=input()
session.get(URL2+str(code))
r2 = session.get(URL2+str(code))
print r2.content
print r2.text