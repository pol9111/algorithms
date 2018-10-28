

def find(lst, x):
    r = 0 # 从左下角开始
    c = len(lst[0]) - 1 # 列(子对象)值的个数等于有几行
    while c >= 0 and r <= len(lst) - 1: # 行减到不超过0, 列加到不超过len-1
        y = l[r][c] # 从左下角开始
        if y == x:
            return True
        elif y > x:
            c -= 1
        elif y < x:
            r += 1
    return False


if __name__ == '__main__':
    l = [[1,     2,    4],     [2,     3,    5], [4,     5,   6],]
    print(find(l, 3))
    print(find(l, 7))