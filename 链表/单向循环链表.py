

class Node:
    """单向循环链表节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None



class SingleCycleLinkList: # 跟单向链表对比, 前四个函数不变, 涉及到增删改的会变, 查不变
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node: # 让第一个节点指向自己
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.__head is None:
            return 0
        cur = self.__head
        count = 0
        while cur.next is not self.__head: # 循环不进入最后一个节点
            count += 1
            cur = cur.next
        return count+1

    def travel(self):
        """遍历链表"""
        if self.__head is None:
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end='')
            cur = cur.next
        print(cur.elem)

    def search(self, elem):
        """链表查找节点是否存在"""
        if self.__head is None:
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == elem:
                return True
            cur = cur.next
        if cur.elem == elem:
            return True
        return False

    def append(self, elem):
        """尾部添加"""
        node = Node(elem)
        if self.__head is None:
            self.__head = node
            node.next = self.__head

        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head


    def add(self, elem):
        """头部添加"""
        node = Node(elem)
        if self.__head is None:
            self.__head = node # 先实例化个Node
            node.next = self.__head # 这个在上面, 会指向None, 只有首次这个在下面
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head # 先让node.next等于久链表
            self.__head = node # 再把根节点指向它



    def insert(self, pos, elem): # 首尾添加特例
        """指定位置添加"""
        if pos <= 0:
            self.add(elem)
        elif pos > self.length()-1:
            self.append(elem)
        else:
            node = Node(elem)
            count = 0
            cur = self.__head
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, elem):
        """删除节点"""
        if self.__head is None:
            return
        cur = self.__head
        if cur.elem == elem: # 若头节点的元素就是要查找的元素item
            if cur.next is not self.__head: # 如果链表不止一个节点
                while cur.next is not self.__head: # 先找到尾节点，将尾节点的next指向第二个节点
                    cur = cur.next
                cur.next = self.__head.next
                self.__head = self.__head.next # 注意这里是删除根节点
            else:
                self.__head = None
        else:
            pre = self.__head
            while cur.next is not self.__head:
                if cur.elem == elem:
                    pre.next = cur.next
                    return
                else: # 本身循环条件在这
                    pre = cur # 保存前一个节点
                    cur = cur.next
                if cur.elem == elem: # cur 指向尾节点 如果是最后一个
                    pre.next = cur.next


if __name__ == '__main__':
    z = SingleCycleLinkList()
    print(z.is_empty())
    print(z.length())
    for i in range(0,2):
        z.append(i)
    # print(z.search(1))
    # z.travel()
    # print(z.length())
    # z.add(3)
    # z.insert(8, 8)
    z.travel()
    z.remove(0)
    z.travel()
