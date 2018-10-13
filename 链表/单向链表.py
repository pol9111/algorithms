

class Node:
    """单向链表节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingLinkList:
    """单向链表"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """链表长度"""
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(cur.elem, end='')
            cur = cur.next
        print('')

    def append(self, elem):
        """尾部添加"""
        node = Node(elem)
        if self.head is None: # None没有next, 先变成跟节点
            self.head = node
        else:
            cur = self.head
            while cur.next is not None: # 注意append是要找到next是空的, 而不是遍历
                cur = cur.next
            cur.next = node

    def add(self, elem):
        """头部添加"""
        node = Node(elem)
        node.next = self.head # 加一个node, 新的next指向整个久链表
        self.head = node # 名称在换回来

    def insert(self, pos, elem):
        """指定位置添加"""
        if pos <= 0:
            self.add(elem)
        elif pos > self.length()-1: # 下标从0开始, len从1开始
            self.append(elem)
        else:
            node = Node(elem)
            count = 0
            pre = self.head
            while count < pos-1: # 到指定位置的前一个停止, 指定位置是给新的节点的
                count += 1
                pre = pre.next # 保存当前节点
            node.next = pre.next # 先将新节点node的next指向插入位置后面的节点
            pre.next = node  # 将插入位置的前一个节点的next指向新节点


    def search(self, elem):
        """链表查找节点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False

    def remove(self, elem):
        """删除节点"""
        cur = self.head
        # if cur.next is None and cur.elem == elem: # 只有一个的
        #     cur.elem = None
        if cur.elem == elem: # 有两个
            self.head = cur.next
        else:
            while cur.next is not None: # 跳过了第一个, 上面做了判断
                pre = cur # 保留上一个
                cur = cur.next # 指向下一个
                if cur.elem == elem:
                    pre.next = cur.next
                    break


def rev(link):
    pre = link.head # 保存当前节点
    cur = link.head.next # 指向下一个节点
    pre.next = None # 当前节点next等于上一个节点
    while cur:
        tmp = cur.next # 临时保存下一个节点
        cur.next = pre # 当前节点next等于上一个节点
        pre = cur # 保存当前节点
        cur = tmp # 指向下一个节点
    link.head = pre # head重新赋值


if __name__ == '__main__':
    s = SingLinkList()
    # print(s.is_empty())
    # print(s.length())
    for i in range(0,2):
        s.append(i)
    # print(s.search(8))
    # s.travel()
    # print(s.length())
    # s.add(0)
    # s.insert(8, 8)
    # s.travel()
    # s.remove(0)
    # s.travel()
    rev(s)
    s.travel()

