from curses.ascii import US
from typing import *
from sortedcontainers import SortedList
from collections import Counter,defaultdict
from functools import cache
from collections import deque

class Solution1:
    def decodeMessage(self, key: str, message: str) -> str:
        subTable=dict()
        subTable[" "]=" "
        visited=set()
        for ch in key:
            if ch==" " or ch in visited:
                continue
            subTable[ch]=chr(ord('a')+len(visited))
            visited.add(ch)
        res=[" "]*len(message)
        for i,ch in enumerate(message):
            res[i]=subTable[message[i]]

        return "".join(i for i in res)
        


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution2:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix=[[-1]*n for _ in range(m)]
        if not head:
            return matrix
        total=m*n
        visited=0
        # 0,1,2,3: TopLeft,TopRight,BottomRight,BottomLeft
        #print(m,n)
        def fill(curr,round=0):
            #print(round)
            nonlocal visited,m,n,matrix,total
            for i in range(round,n-round):
                if curr and visited<total:
                    matrix[round][i]=curr.val
                    curr=curr.next
                    total+=1
                else:
                    return
            for i in range(round+1,m-round):
                if curr and visited<total:
                    matrix[i][n-1-round]=curr.val
                    curr=curr.next
                    total+=1
                else:
                    return
            for i in range(round+1,n-round):
                if curr and visited<total:
                    matrix[m-1-round][n-1-i]=curr.val
                    curr=curr.next
                    total+=1
                else:
                    return
            for i in range(round+1,m-round-1):
                if curr and visited<total:
                    matrix[m-1-i][round]=curr.val
                    curr=curr.next
                    total+=1
                else:
                    return
            if curr and visited<total:
                fill(curr,round+1)
        fill(head)
        return matrix

class Solution3:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        modulo=10**9+7
        store=deque([0]*(forget+1))
        store[forget]=1
        storeSum=sum(store)
        delaySum=0
        for i in range(n-1):
            #print(storeSum,delaySum,store)
            storeSum=(storeSum-store[1])%modulo
            delaySum=(delaySum-store[1])%modulo
            store.popleft()
            delaySum=(delaySum+store[forget-delay])%modulo
            store.append(delaySum)
            storeSum=(storeSum+delaySum)%modulo
        return storeSum%modulo

class Solution:
    '''
    def countPaths(self, grid: List[List[int]]) -> int: # TLE (sadly)
        modulo=10**9+7
        m=len(grid)
        n=len(grid[0])
        def BFS(i,j):
            nonlocal m,n
            total=1
            visited=set()
            queue=deque()
            queue.append((i,j))
            while queue:
                i,j=queue.popleft()
                currValue=grid[i][j]
                visited.add((i,j))
                adj=[]
                for (ni,nj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=ni<=m-1 and 0<=nj<=n-1 and grid[ni][nj]>currValue:
                        adj.append((ni,nj))
                for V in adj:
                    visited.add(V)
                    queue.append(V)
                    total+=1
                    total%=modulo
            return total 
        
        total=0   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total+=BFS(i,j)
                total%=modulo
        return total%modulo
    '''
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        modulo=10**9+7
        @cache
        def dp(i,j):
            total=1
            next=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for ni,nj in next:
                if 0<=ni<=m-1 and 0<=nj<=n-1 and grid[ni][nj]>grid[i][j]:
                    total+=dp(ni,nj)
                    total%=modulo
            return total
        total=0
        for i in range(m):
            for j in range(n):
                total+=dp(i,j)
                total%=modulo
        return total
