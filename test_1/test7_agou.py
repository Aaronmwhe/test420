# coding:utf-8
import requests
import re
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()

# 登陆拉勾网

s = requests.session()
url1 = "https://passport.lagou.com/login/login.html"

r1 = s.get(url1,verify=False)
print(r1.status_code)
# print(r1.content.decode("utf-8"))
res = r1.content.decode("utf-8")
soup= BeautifulSoup(r1.content,"html.parser")
s1 = soup.find_all("script")
# for i in s1:
# #  print(i)
print(s1[1].string)
a = s1[1].string
X_Anti_Forge_Token = re.findall("_Token = \'(.+?)\'", a)
print(X_Anti_Forge_Token[0])
X_Anti_Forge_Cod = re.findall("e_Code = \'(.+?)\'", a)
print(X_Anti_Forge_Cod[0])
# result = re.findall("<script>(.+?)\</script>", res)
# print(result)
url = "https://passport.lagou.com/login/login.json"
h = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
"X_Anti_Forge_Token":"",
"X_Anti_Forge_Cod":""

      }
body = {
   "isValidate": "true",
    "username": "13414140950",
    "password": "a658cefe791f6c870413ea5fb6420187",
    "request_form_verifyCode": "",
    "submit": "",
    "challenge": "91c87059bb6c17f6718bbd936d9655e2"

    }

r = s.post(url, data=body,headers=h, verify=False)
print(r.status_code)
print(r.content.decode("utf-8"))

#    <!-- 页面样式 -->    <!-- 动态token，防御伪造请求，重复提交 -->
#     <script>
#     window.X_Anti_Forge_Token = '8ddb320f-82d5-4147-a128-f1bd5ef671fa';
#     window.X_Anti_Forge_Code = '48340395';
# </script>
#
#     <!-- H5  -->
