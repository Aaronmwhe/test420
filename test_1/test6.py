# coding:utf-8
import requests

url ="http://192.168.2.107/zentao/user-login.html"

s = requests.get(url)
print(s.status_code)
print(s.cookies)  #JAR的格式
c = dict(s.cookies) #字典格式

