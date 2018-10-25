import random


def counting_sort(arr, k):  # k = max(arr)
    n = len(arr)  # 计算a序列的长度
    rst = [0 for _ in range(n)]  # 设置输出序列并初始化为0
    c = [0 for _ in range(k + 1)]  # 设置计数序列并初始化为0
    for j in arr: # 先进行一遍计数, 计算每个数出现次数
        c[j] = c[j] + 1 # c[j]即当前值总个数
    for i in range(1, len(c)): # 计数序列每个数加上前一个数, 最终位置区间=(前面所有数出现次数, 自己出现次数)
        c[i] = c[i] + c[i-1]
    # for i in range(len(c)-2, -1, -1): # 降序, 从后往前计数
    #     c[i] = c[i] + c[i+1]
    for j in arr: # 不稳定, 倒着拿出来就变成稳定的
        rst[c[j] - 1] = j # c[j] - 1(表示下标减一), 把j放到对应位置
        c[j] = c[j] - 1 # c[j]当前值总个数-1
    return rst



if __name__ == '__main__':
    l = list(range(100))
    random.shuffle(l)
    print(l)
    z = counting_sort(l, max(l))
    print(z)


"""
计数排序
假设n个输入元素中的每一个都是在0到k区间内的一个整数，其中k为某个整数。
对每一个输入元素x，确定小于x的元素个数，利用这一信息，就可以直接把x放到它在输出数组中的位置上了。

稳定性 Y
空间复杂度：O(k+n)
最差/平均/最优时间复杂度：O(k+n)
"""