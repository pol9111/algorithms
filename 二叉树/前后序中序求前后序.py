

def rebuildpreorder(preList, midList, afterList):
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0] # 前后序先拿出一个根节点
    mid = midList.index(root) # 找到根节点在中序下标
    rebuildpreorder(preList[1:mid + 1], midList[:mid], afterList) # 前部分分出来的对应前后序和中序的列表
    rebuildpreorder(preList[mid + 1:], midList[mid + 1:], afterList) # 后部分分出来的对应前后序和中序的列表
    afterList.append(root)


def rebuildpostorder(preList, midList, afterList):
    if len(afterList) == 0:
        return
    elif len(afterList) == 1:
        preList.append(afterList[-1])
        return
    root = afterList[-1] # 前后序先拿出一个根节点
    mid = midList.index(root) # 找到根节点在中序下标
    preList.append(root)
    rebuildpostorder(preList, midList[:mid], afterList[:mid])  # 前部分分出来的对应前后序和中序的列表
    rebuildpostorder(preList,  midList[mid + 1:], afterList[mid:-1]) # 后部分分出来的对应前后序和中序的列表

# 二合一版本
def rebuilder(pre_aftList, midList, rebuildList, index=0):
    """求前后序遍历列表"""
    if len(pre_aftList) is 0:
        return
    elif len(pre_aftList) is 1:
        rebuildList.append(pre_aftList[index])
        return
    root = pre_aftList[index] # 前后序先拿出一个根节点, 前序列表拿第一个, 后序最后一个
    mid = midList.index(root)
    rebuilder(pre_aftList[1:mid+1], midList[:mid], rebuildList) # 前部分分出来的对应前后序和中序的列表
    rebuilder(pre_aftList[mid+1:], midList[mid+1:], rebuildList) # 后部分分出来的对应前后序和中序的列表
    rebuildList.append(root) # 求后序写递归后, 求前序写递归前

    # rebuildList.append(root) # 求后序写递归后, 求前序写递归前
    # rebuilder(pre_aftList[:mid], midList[:mid], rebuildList)  # 前部分分出来的对应前后序和中序的列表
    # rebuilder(pre_aftList[mid:-1], midList[mid+1:], rebuildList)  # 后部分分出来的对应

    # midList不要取到mid值, 前序不要取到第一个所以 mid都要加一, 后序不取到最后一个

if __name__ == '__main__':

    preorder = [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
    inorder = [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
    postorder = [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]
    rebuildList = []

    rebuilder(preorder, inorder, rebuildList)
    print(rebuildList)

    # rebuildpreorder(preorder, inorder, r_postorder)
    # print(r_postorder)
    # rebuildpostorder(r_preorder, inorder, postorder)
    # print(r_preorder)

"""
前后序中序求前后序
4个参数, 前后序, 中序, 重建, 下标=0
if len=0
if len=1
从前后序拿出根
从中序拿出下标
递归前部分
递归后部分
append(求后序写递归后)
"""