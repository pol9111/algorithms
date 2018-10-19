import random


def quick_sort(lst, start, end):
    """运行快排"""
    if start < end: # 递归停止条件, 左下标和右下标相遇即停止
        mid = sift(lst, start, end) # 给下面递归提供的中间值， 一直做分割patition
        quick_sort(lst, start, mid - 1) # 中间值左边一直做递归直到，left = right
        quick_sort(lst, mid + 1, end) # 中间值右边一直做递归直到，left = right
                                            # mid -+ 1 不要中间值, 剩下的区间

def sift(lst, left, right):
    """快排分割"""
    mid = lst[left] # 先把一个值拿出来, left列表第一个值
    while left < right: # 让快速排序一直运行的条件， 左下标和右下标相遇即停止
        while left < right and lst[right] >= mid: # 之所以要在再加left < right， 可能在一个while里面把L/R减到-1
            right -= 1 # 如果满足条件再往前， 跟前一个值比较
        lst[left] = lst[right] # 如果不满足条件， 把右边的值放去左边， 就是给左边的位置赋值
        while left < right and lst[left] <= mid:
            left += 1
        lst[right] = lst[left]
    lst[left] = mid # 把早先拿走的值放到停顿的那个位置
    return left # 返回值作为中间值mid


def quicksort(lst):
    """较快的快排"""
    if len(lst) < 2:
        return lst
    else:
        midpivot = lst[0]
        lessbeforemidpivot = [i for i in lst[1:] if i<=midpivot]
        biggerafterpivot = [i for i in lst[1:] if i > midpivot]
        finallylist = quicksort(lessbeforemidpivot)+[midpivot]+quicksort(biggerafterpivot)
        return finallylist


data = list(range(100))
random.shuffle(data)
print(data)

quick_sort(data, 0, len(data) - 1)
print(data)

rst = quicksort(data)
print(rst)


"""
快排
版本一(左右指针)
2个函数
1. 指定拆分值等于比对函数, 递归 分割左右列表(参数0, len-1)
2. 比对函数


详细
1. 函数
重新指定中间值等于比对函数(排序了)的返回值
递归 分割左右列表


2. 函数
指定中间值
while循环
	左指针比右指针小(不相遇) and 左右值比对
	右相反
中间值等于相遇位置
返回相遇位置(作为拆分中间值)




版本二(空间换时间)
1个函数
1. 递归 左列表+[mid]+右列表


详细
1. 函数
递归结束条件, 列表小于2返回列表
指定中间值
把小于等于中间值的值左列表
把大于中间值的值右列表
最终列表 = 递归 左列表+[mid]+右列表
返回最终列表
"""