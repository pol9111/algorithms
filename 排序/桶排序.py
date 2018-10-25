import random


def bucket_sort(arr):
    buckets = [0] * ((max(arr) - min(arr)) + 1)  # 初始化桶元素为0
    for i in range(len(arr)):
        buckets[arr[i] - min(arr)] += 1  # 遍历数组a，在桶的相应位置(arr[i] - min(arr))累加值
    rst = []    # 当前值-最小值即=桶位置
    for j in range(len(buckets)): # 遍历桶, 拿出并放到新的列表, 升序
    # for i in range(len(buckets)-1, -1, -1): # 降序
        if buckets[j] != 0:
            rst += [j + min(arr)] * buckets[j] # i+min(a)=arr的值 * 桶的值(arr的值的个数), 放到rst列表里
    return rst      # 桶位置+最小值=当前值


if __name__ == '__main__':
    l = list(range(100))
    random.shuffle(l)
    print(l)
    a = bucket_sort(l)
    print(a)



"""
桶排序
假设输入是由一个随机过程产生，该过程将元素均与、独立地分布在[0,m)区间上

将[0,m)区间划分为BUCKET_NUM个相同大小的子区间（桶）
将n个输入数分别放到各个桶中
对每个桶中的数进行排序
遍历每个桶，按照次序把各个桶中的元素列出即可

稳定性 Y
空间复杂度：O(n*k)
最差时间复杂度：O(n^2), 平均时间复杂度：O(n+k)
"""
