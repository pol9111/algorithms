import random


def radix_sort(arr, d): # 默认三位数，如果是四位数，则d=4，以此类推
    for i in range(d):  # d轮排序 i从小到大, 次位优先, 即每趟就完成一个位的排序
        bucket_list = [[] for _ in range(10)]  # 因每一位数字都是0~9，建10个桶
        for j in arr:
            bucket_list[j // (10 ** i) % 10].append(j) # 升序 s[表示该放到拿] j(当前值)//10 ** i(当前位)%10(十进制, 即桶个数)
            # s[abs((j // (10 ** i) % 10)-9)].append(j) # 降序, 把9桶对应0桶, 8桶对应1桶
        arr = [a for b in bucket_list for a in b] # b=bucket(桶), s=所有桶的列表, a无意义, 按桶顺序拿出, 即保存当前排序进度
    return arr


if __name__ == '__main__':
    l = list(range(1000))
    random.shuffle(l)
    print(l)
    z = radix_sort(l, 3)
    print(z)


"""
基数排序
先按最低有效位进行排序。

将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。
然后，从最低位开始，依次进行一次排序。
这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列。

稳定性 Y
空间复杂度：O(k+n) , n是排序元素个数，k是单位数字最大值
空间复杂度：O(d*n), n是排序元素个数，d是数字位数
"""