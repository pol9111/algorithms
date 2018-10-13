import random


l = list(range(100))
random.shuffle(l)
print(l)

def shell_sort(lst):
    gap = len(lst) // 2
    while gap > 0: # 一直到gap等于1, gap != 1的话少排一次
        for i in range(gap, len(lst)): # 把1变成gap
            j = i
            while j >= gap and lst[j-gap] > lst[j]:
                lst[j-gap], lst[j] = lst[j], lst[j-gap]
                j -= gap
        gap = gap // 2


def insert_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1


def insert_sort2(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1): # 有序区
            if lst[j] < lst[j-1]: # 如果满足条件就交换
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else: # 不满足时, 即前面的值都比我大/小
                break

insert_sort2(l)
print(l)

"""
希尔排序
设置gap
while gap大于0
	版本二的插入排序
把插入的1变成ga
"""