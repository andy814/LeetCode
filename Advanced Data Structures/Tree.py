import collections
from logging.config import valid_ident

# Traverse:
def preorder(root):
    stack = [root]
    while stack:
        s = stack.pop()
        if s:
            print(s.val)
            stack.append(s.right)
            stack.append(s.left)

def inorder(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val)
        root = root.right

def postorder(root):
    stack = []
    while stack or root:
        while root:                 # 下行循环，直到找到第一个叶子节点
            stack.append(root)
            if root.left:           # 能左就左，不能左就右
                root = root.left 
            else:
                root = root.right     
        s = stack.pop()
        print(s.val)
        if stack and s == stack[-1].left: 
            root = stack[-1].right
        else:
            root = None

'''
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
n5=ListNode(5)
n6=ListNode(6)
n7=ListNode(7)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

preOrder2(n1)
inOrder2(n1)
postOrder2(n1)
'''