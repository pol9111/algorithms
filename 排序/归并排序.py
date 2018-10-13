import random


def merge_sort(lst):
    """归并排序"""
    if len(lst) <= 1: # 分开到列表只剩下一个值
        return lst
    num = len(lst) // 2 # 每次对半分开
    left = merge_sort(lst[:num]) # 分开一个个左列表
    right = merge_sort(lst[num:]) # 分开一个个右列表
    return merge(left, right) # 分开完之后, 一个个归并


def merge(left, right):
    """归并部分"""
    l, r = 0, 0 # 左右指针
    result = [] # 合并后的新表
    while l < len(left) and r < len(right): # 移动左右指针的值
        if left[l] < right[r]: # 比较左右两边的值
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:] # 最后有一个值没有对手比较, 不确定在哪个表
    result += right[r:] # 左右有个指针会移出去(大于下标), 有个列表是空的
    return result


if __name__ == '__main__':
    li = list(range(100))
    random.shuffle(li)
    print(li)
    li_ = merge_sort(li)
    print(li_)


"""
归并排序
2个函数
1. 递归分开列表, return合并列表函数
2. 合并列表函数


详细
1. 函数
递归停止条件, 分开列表只有一个值
指定分割值
左列表分割递归
右列表分割递归
返回 合并列表函数


2. 函数
设定左右指针初始值
设定接受列表为空


左右列表比对循环
指针不超过左右列表长度
if 左右值比对
	加入接受列表
	左指针加一
else 
	相反
接受列表 += 剩下的值
返回 接受列表
"""