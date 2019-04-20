# coding:utf-8
import requests
import urllib3
#  https://i.cnblogs.com/EditPosts.aspx?opt=1
# allow_redirects=False
urllib3.disable_warnings()
url="https://i.cnblogs.com/EditPosts.aspx?opt=1"
r = requests.get(url, verify=False)
print(r.history)  # 获取其中一个返回
print(r.url)

r1 =r.history[0]