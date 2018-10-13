
a = [1,2,3,7,9,1,5]
b = [4,5,7,9,1,5]

for i in range(1,min(len(a),len(b))):
    if i==1 and a[-1] != b[-1]:
        print("No")
        break
    else:
        if a[-i] != b[-i]:
            print("交叉节点：",a[-i+1])
            break
        else:
            pass


#
#
# # 另外一种比较正规的方法，构造链表类
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# def node(l1, l2):
#     length1, length2 = 0, 0
#     # 求两个链表长度
#     while l1.next:
#         l1 = l1.next
#         length1 += 1
#     while l2.next:
#         l2 = l2.next
#         length2 += 1
#     # 长的链表先走
#     if length1 > length2:
#         for _ in range(length1 - length2):
#             l1 = l1.next
#     else:
#         for _ in range(length2 - length1):
#             l2 = l2.next
#     while l1 and l2:
#         if l1.next == l2.next:
#             return l1.next
#         else:
#             l1 = l1.next
#             l2 = l2.next
#
#
# # 修改了一下:
#
# #coding:utf-8
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# def node(l1, l2):
#     length1, length2 = 0, 0
#     # 求两个链表长度
#     while l1.next:
#         l1 = l1.next#尾节点
#         length1 += 1
#     while l2.next:
#         l2 = l2.next#尾节点
#         length2 += 1
#
#     #如果相交
#     if l1.next == l2.next:
#         # 长的链表先走
#         if length1 > length2:
#             for _ in range(length1 - length2):
#                 l1 = l1.next
#             return l1#返回交点
#         else:
#             for _ in range(length2 - length1):
#                 l2 = l2.next
#             return l2#返回交点
#     # 如果不相交
#     else:
#         return