
def merge(arr1, arr2):
    rst = []
    while len(arr1) and len(arr2): # 两个列表同时存在元素的话就能比较
        if arr1[0] < arr2[0]:
            rst.append(arr1[0])
            del arr1[0]
        else:
            rst.append(arr2[0])
            del arr2[0]
    rst.extend(arr1)
    rst.extend(arr2)
    return rst


a = [1,2,3,7]
b = [3,4,5]
c = merge(a, b)
print(c)







