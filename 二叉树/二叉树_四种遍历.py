from collections import deque


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

    def breadth_travel(self, node):
        """利用队列实现树的层次遍历"""
        if node is None: # 没有根节点的情况
            return
        queue = deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            print(cur.elem, end=' ')
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')

def maxDepth(node):
    """最大树深"""
    if not node:
        return 0
    return max(maxDepth(node.lchild), maxDepth(node.rchild)) + 1


def isSameTree(p, q):
    """两个树是否相同"""
    if p is None and q is None:
        return True
    elif p and q:
        return p.elem == q.elem and isSameTree(p.lchild, q.lchild) and isSameTree(p.rchild, q.rchild)
    else:
        return False


if __name__ == '__main__':

    tree = Tree()
    for i in range(0, 10):
        tree.add(i)

    print('\n', '层次遍历', end='')
    tree.breadth_travel(tree.root)
    print('\n', '先序遍历', end='')
    tree.preorder(tree.root)
    print('\n', '中序遍历', end='')
    tree.inorder(tree.root)
    print('\n', '后序遍历', end='')
    tree.postorder(tree.root)

    depth = maxDepth(tree.root)
    print('\n', '最大树深: ', depth, end='')

    tree2 = Tree()
    for i in range(0, 10):
        tree2.add(i)
    rst = isSameTree(tree.root, tree2.root)
    print('\n', '两个树是否相同: ', rst, end='')