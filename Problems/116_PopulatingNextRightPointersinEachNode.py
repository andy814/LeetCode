from typing import *
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        count=1
        level=0
        queue=deque([root])
        prev=None
        while queue:
            top=queue.popleft()
            #print(top.val)
            count-=1
            if prev:
                prev.next=top
            prev=top

            if count==0:
                level+=1
                count=2**level
                top.next=None
                prev=None
            
            if top.left:
                queue.append(top.left)
                queue.append(top.right)
        
        return root