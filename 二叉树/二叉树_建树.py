from collections import deque
import unittest


class Node:
    """二叉树的节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None): # 一个节点实例具有三个属性: 值, 左子节点, 右子节点
        self.elem = elem # 准备存入的数据
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """二叉树类"""
    def __init__(self):
        self.root = None

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root is None: # 如果树是空的，则对根节点赋值
            self.root = node # 变成一个节点实例, elem值为传入elem, 同时具有lchild, rchild两个属性, 值为None
        else:
            queue = deque() # deque作为双向队列比list好
            queue.append(self.root) # 对已有的节点进行层次遍历
            while queue:
                cur = queue.popleft() # 弹出队列的一个节点
                if cur.lchild is None:
                    cur.lchild = node # 该节点lchild变成一个节点实例, 新的节点值为传入elem, 同时具有lchild, rchild两个属性, 值为None
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else: # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.elem, end='\t')
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


class Test(unittest.TestCase):
    def testTree(self):
        tree = Tree()
        for i in range(1000):
            tree.add(i)

        tree.breadth_travel()


if __name__ == "__main__":

    unittest.main()