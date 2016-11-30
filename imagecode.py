#-*- coding: UTF-8 -*-
import pytesseract
from PIL import Image

#模糊替换
rep = {'O': '0',
               'I': '1',
               'L': '1',
               'Z': '2',
               'S': '8',
               'Q': '0',
               '}': '7',
               '*': '',
               'E': '6',
               ']': '0',
               '`': '',
               'B': '8',
               '\\': '',
               '.': '',
               ' ': '',
               '(1':'0',
               '’': ''
               }
# 把彩色图像转化为灰度图像
im = Image.open('1610.jpg')
imgry = im.convert('L')

# 图片去噪
threshold = 120
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.save('1530_1.jpg')
#out.show()

#获取验证码
image = Image.open('1530_1.jpg')
vcode = pytesseract.image_to_string(image)
for r in rep:
    vcode = vcode.replace(r,rep[r])
print vcode

