

class Node:
    """双向链表节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList: # 跟单向链表对比, 前四个函数不变, 涉及到增删改的会变, 查不变
    """双向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end='')
            cur = cur.next
        print('')

    def search(self, elem):
        """链表查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False

    def append(self, elem):
        """尾部添加"""
        node = Node(elem) # 增改都要实例化一个Node(elem)
        if self.__head is None: # None没有next, 先变成跟节点
            self.__head = node
        else:
            cur  = self.__head
            while cur.next is not None: # 注意append是要找到next是空的, 而不是遍历
                cur = cur.next
            cur.next = node
            node.prev = cur

    def add(self, elem):
        """头部添加"""
        node = Node(elem)
        if self.__head is None: # None没有next, 先变成跟节点
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node  # 将__head 指向node(根节点换了)


    def insert(self, pos, elem): # 首尾添加特例
        """指定位置添加"""
        if pos <= 0:
            self.add(elem)
        elif pos > self.length()-1:
            self.append(elem)
        else:
            node = Node(elem)
            cur = self.__head
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node # 注意这个在上面一个的话, 上面要改成node.next.prev=

    def remove(self, elem):
        """删除节点"""
        if self.__head is None:
            return
        else:
            cur = self.__head
            if cur.elem == elem:
                if cur.next is None:
                    self.__head = None
                else:
                    cur.next.prev = None
                    self.__head = cur.next
                return
        while cur is not None: # 进入此循环需要三个节点
            if cur.elem == elem:
                # 将cur的前一个节点的next指向cur的后一个节点
                cur.prev.next = cur.next
                if cur.next: # 最后一个的next没有prev属性
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                break
            cur = cur.next


if __name__ == '__main__':
    z = DoubleLinkList()
    # print(s.is_empty())
    # print(s.length())
    for i in range(0,2):
        z.append(i)
    # print(s.search(8))
    # s.travel()
    # print(s.length())
    # s.add(0)
    # s.insert(8, 8)
    z.travel()
    z.remove(0)
    z.travel()
