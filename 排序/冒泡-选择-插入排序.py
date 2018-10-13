
import random


l = list(range(100))
random.shuffle(l)
print(l)


def bubble_sort(lst):
    """冒泡排序"""
    for i in range(len(lst) - 1): # 需要排序的列表长度（几趟）, 跟j + 1比较 所以len-1, 最底下那个数已经在本来位置
        exchange = 0
        for j in range(len(lst) - 1 - i): # 每趟的长度（发生几次比较）
            if lst[j] > lst[j + 1]: # 比较前后二个值的大小
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # 交换前后两个值的位置
                exchange = 1
        if exchange is 0: # 优化, 走完一趟没有发生交换, 即是结果
            return lst
    return lst # 返回有序列表


# bubble_sort(l)
# print(l)


def select_sort(lst):
    """选择排序"""
    for i in range(len(lst) - 1): # 需要排序的列表长度（几趟）， 最后一个没东西比较，就在他本来位置
        tmp = i # set 一个默认最小值
        for j in range(i + 1, len(lst)): # 从i后面一个值开始比较到最后一个值
            if lst[j] < lst[tmp]:
                tmp = j # 最小值的下标变为j
        lst[i], lst[tmp] = lst[tmp], lst[i] # 旧的放回去继续比较， 新的拿出来归位
# 1.要判断的i值 2.i or j值 3.旧j位置or原本最小值位置  4.最小值的位置
        # 列表 值 互换位置
    return lst

# select_sort(l)
# print(l)


# def insert_sort(lst):
#     """插入排序"""
#     for i in range(1, len(lst)): # 从第二个开始
#         tmp = lst[i] # 为什么要设置tmp， 因为在while循环的一行lst[j]的值换了
#         j = i -1 # 下面都是j 和 tmp
#         while j >= 0 and lst[j] > tmp:# 拿tmp在有序列表里比,
#             lst[j + 1] = lst[j] # 每次while后面空位被前面一位赋值(把前面的数扔到后面)
#             j = j - 1 # 让下标j 一直往前
#         lst[j + 1] = tmp # 停止时的空位被tmp替换(一直拿来比对的值)
#     return lst

# insert_sort(l)
# print(l)


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