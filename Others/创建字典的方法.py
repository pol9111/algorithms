# 直接创建
dict1 = {'name':'earth', 'port':'80'}

# 工厂方法
items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)
print(dict2)

# fromkeys()方法
l = ('x', 'y', 'z')
dict3 = {}.fromkeys(l, -1)
print(dict3)


