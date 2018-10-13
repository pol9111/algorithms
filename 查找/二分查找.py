

def binary_search(lst, item):
    """二分查找, 递归"""
    n = len(lst)
    if n > 0:
        mid = n // 2
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            return binary_search(lst[:mid], item)
        else:
            return binary_search(lst[mid+1:], item)
    return False


def binary_search2(lst, item):
    """二分查找, 非递归"""
    start = 0
    end = len(lst) - 1
    while start < end: # 直到等于或不大于
        mid = (start + end) // 2
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == '__main__':
    data = [2, 4, 33, 44, 55, 66, 77, 88, 99, 100]
    print(binary_search(data, 33))
    print(binary_search(data, 101))
    print(binary_search2(data, 33))
    print(binary_search2(data, 101))

