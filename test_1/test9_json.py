# coding:utf-8
import json
# print(help(json))

a = None

aa = json.dumps(a)  #转化为JSON格式
print(type(aa))
print(aa)  #null

b=False
bb=json.dumps(b)
print(type(bb))
print(bb)

c= "hello world"
print(json.dumps(c))

d = [None, 112, "bb"]
dd = json.dumps(d)  #变成json格式
print(type(dd))
print(dd)

e = (None, 112, "bb")
print(json.dumps(e))

# 如，[{"a":true,"b:null}]
qq = {"a": True, "b": None}
print(json.dumps(qq))