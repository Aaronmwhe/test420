# coding:utf-8
import json
import requests
s = requests.session()
# b = '{"a": true, "b": null}'  # json格式的dict
# print(json.loads(b))
# c = '{"a": True, "b": None}'  # python 标准dict格式字符串
# print(eval(c))
url = "http://japi.juhe.cn/qqevaluate/qq"
par = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq": "229025284"  #  283340479
}

r = s.get(url, params=par)
print(r.text)
url1 = r.text
# print(type(url1))
# print(eval(url1))
# print(json.loads(url1))

# request 里面自带了json解释器
url1 = r.json()
print(url1)
# print(url1['result']['data'])
