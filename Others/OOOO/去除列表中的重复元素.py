
# 用集合
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
print(l2)


# 列表推导式
l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if i not in l2]
print(l2)


# 用字典
l1 = ['b','c','d','b','c','a','a']
l2 = {}.fromkeys(l1).keys()
print(l2)


# 保持顺序
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)





