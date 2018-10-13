

def Solution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(Solution1('abcd','dcba'))

def Solution2(s1,s2):
    arr1 = list(s1)
    arr2 = list(s2)

    arr1.sort()
    arr2.sort()

    pos = 0

    while pos < len(arr1):
        if arr1[pos] == arr2[pos]:
            pos += 1
        else:
            return False
    return True

print(Solution2('abcde','edcbg'))

def Solution3(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(Solution3('apple','pleap'))