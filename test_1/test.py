#coding:utf-8
import requests
url ="http://japi.juhe.cn/qqevaluate/qq"
par = {
    "key":"8dbee1fcd8627fb6699bce7b986adc45",
    "qq":"229025284"
}

r = requests.get(url,params=par)
print(r.status_code)
print(r.headers)
print(r.text)