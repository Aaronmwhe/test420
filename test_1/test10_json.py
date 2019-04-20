# coding:utf-8
import json

a = '[{"a":true,"b":null}]'
print(json.loads(a))  #JSON格式解释

b = '{"a": true, "b": null}'
print((json.loads(b)))
print(str(b))

b1 ='{"a":True,"b":None}' #pthon 标准dict格式字符串
print(eval(b1))