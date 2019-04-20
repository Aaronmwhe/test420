# coding utf-8
a =12

print(type(a))  # None,bool,int,float,str,list,tuple,dict
g = []  # list 可变的对象
print(type(g))

g.append(a)
g.append([56, 56, 32])
print(g)

h= (45, 54)  # tuple 不可变的对象
print(type(h))
print(h[-1])

w = {
    "a": 1,
    "sdf": "sdf"
    }
# 字典是无序的，key是唯一的
print(w["a"])
