# Source: https://gist.github.com/HaoyangFan/1b3ffb0b313ea08f7e77c2c4d7e977c7
import itertools
from collections import deque

'''
A monotonous decreasing (based on compartor passed) stack
'''

class MonoStack(object):
    # comp: the comparator function
    def __init__(self, comp=None):
        if comp==None:
            def comp(v1, v2): # 单减
                return v1 - v2
            self.comp=comp
        else:
            self.comp = comp
        self.stack = deque()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        assert not self.isEmpty()
        return self.stack[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.stack.pop()

    def push(self, v):
        rst = []  # used to hold elements popped off during this process
        # while stack is not empty and its topmost element is smaller than
        # current element
        while not self.isEmpty() and self.comp(self.peek(), v) <= 0: # 严格单调性，<0是不严格
            rst.append(self.pop())
        self.stack.append(v)
        return rst

    def __str__(self):
        if self.isEmpty():
            return 'current monotone stack is empty'
        s = 'current monotone stack: ['
        for v in itertools.islice(self.stack, len(self.stack) - 1):
            s += '{0}, '.format(v)
        s += '{0}]'.format(self.stack[-1])
        return s


# another version, the ans[] records next greater element
if __name__ == "__main__":
    m=[]
    array=[2,1,2,4,3,1]
    ans=[0]*len(array) 
    for i in range(len(array)-1,-1,-1): # step -1 for first num on the right, step 1 for first num on the left
        while m and m[-1]<=array[i]: # <= for find next greater, < for find next greater or equal, >= for find next smaller, > for find next smaller or equal
            m.pop()
        ans[i]=-1 if not m else m[-1]
        m.append(array[i])
    print(ans)


# another version, the ans[] records next greater element's index
if __name__ == "__main__":
    m=[]
    array=[2,1,2,4,3,1]
    ans=[0]*len(array) 
    for i in range(len(array)-1,-1,-1): # step -1 for first num on the right, step 1 for first num on the left
        while m and array[m[-1]]<=array[i]: # <= for find next greater, < for find next greater or equal, >= for find next smaller, > for find next smaller or equal
            m.pop()
        ans[i]=-1 if not m else m[-1]
        m.append(i)
    print(ans)