# coding:utf-8
import requests
import re
s= requests.session()
print(s.cookies)
url = "http://192.168.2.107/zentao/user-login-L3plbnRhby9teS5odG1s.html"
s1=s.get(url)
print(s.cookies)
# cook1 =s.cookies
# print(cook1)
h = {
    "Content-Type": "application/x-www-form-urlencoded",
   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
     # "Cookie": "lang=zh-cn; device=desktop; theme=default; windowWidth=1073; windowHeight=775; zentaosid=oeulmv366s8ic7hruug4qujec2"

    }
body = {
      "account": "admin",
      "password": "57cb60fcb3be2932505b997234227df3",
      "keepLogin[]": "on",
      "referer": "/zentao/my.html",
       }

r = s.post(url, data=body, headers=h)
print (r.url)
print (r.status_code)
print (r.content.decode("utf-8"))
res = r.content.decode("utf-8")
try:
    # 正则提取
    result = re.findall("alert\(\'(.+?)\'\)", res)
    print(result[0])
except:
    print("登录成功")

cook = r.cookies
print(cook)
url1= "http://192.168.2.107/zentao/my/"
my=requests.get(url, cookies=cook)
print(my.status_code)
# print(my.text)



