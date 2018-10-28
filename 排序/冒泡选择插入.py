import random


l = list(range(100))
random.shuffle(l)
print(l)


def bubble_sort(lst):
    """冒泡排序"""
    for i in range(len(lst) - 1): # 需要排序的列表长度（一趟）, 跟j + 1比较 所以len-1, 最底下那个数已经在本来位置
        exchange = 0
        for j in range(len(lst) - 1 - i): # 每趟的长度（步长）
            if lst[j] > lst[j + 1]: # 比较前后二个值的大小
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # 交换前后两个值的位置
                exchange = 1
        if exchange is 0:
            break


bubble_sort(l)
print(l)


def select_sort(lst):
    for i in range(len(lst) - 1):
        # 需要排序的列表长度（一趟）， 最后一个没东西比较，就在他本来位置
        tmp = i # set 一个默认最小值
        for j in range(i + 1, len(lst)): # 从i后面一个值开始比较到最后一个值
            if lst[j] < lst[tmp]:
                tmp = j # 最小值的下标变为j
        lst[i], lst[tmp] = lst[tmp], lst[i]
        # 旧的放回去继续比较， 新的拿出来归位
# 1.要判断的i值 2.i or j值 3.旧j位置or原本最小值位置  4.最小值的位置
        # 列表 值 互换位置


select_sort(l)
print(l)


def insert_sort(lst):
    """插入排序"""
    for i in range(1, len(lst)):
        for j in range(i, 0, -1): # 有序区
            if lst[j] < lst[j-1]: # 如果满足条件就交换
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else: # 不满足时, 即前面的值都比我大/小
                break




insert_sort(l)
print(l)


def insert_sort(lst):
    """插入排序"""
    for i in range(1, len(lst)):
        j = i
        while j >= 1 and lst[j] < lst[j-1]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
            j -= 1


"""
冒泡排序(扔后面)
2个for循环
1. for几趟(总长)
2. for每趟长度(每次少一个)
优化


选择排序(扔前面)
2个for循环
1. for几趟(总长)
临时下标
2. for从i后, 值比对, 换临时下标
i 和临时下标换位置


插入排序(扔前面)
2个for循环
1. for几趟, 从1开始
2. for跟有序区比对, 不发生改变即停止
"""