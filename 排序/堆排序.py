

def heap_sort(arr):
    # 第一次建堆从最后一个有子节点的孩子开始 调整最大堆 (i-1)/2
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        sift(arr, start, len(arr) - 1)

    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) -1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift(arr, 0, end - 1)



def sift(arr, start, end):
    root = start # 首先指定第一个父节点
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1
        # 父节点一直跟孩子比到最后
        if child > end: # 如果子节点下标大于堆最后一个下标
            break

        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]

            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候, 退出
            break


def main():
    l = [7, 95, 73, 65, 60, 77, 28, 62, 43]
    # [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    # l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(l)
    heap_sort(l)
    print(l)


if __name__ == "__main__":
    main()



"""
堆排序
2个函数
1. 循环第一次建堆, 循环每次出最后一个值 两个for循环
2. 建堆函数 while+4个判断


详细
1. 函数(两个for循环)
从最后一个有子节点的节点开始 first
for循环 range(first, -1, -1)
	sift(lst, i, len-1)

for循环 range(len-1, 0, -1)
	sift(lst, 0, end-1)
	
2. 函数(while+4个判断)
指定第一个父节点
while循环
指定子节点
1 if 子节点不超过最后
2 if 左右两个子节点比对
3 if 父节点子节点比对
	重新指定父节点
4 break
"""