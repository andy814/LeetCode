import collections
from email.policy import default
import functools
from typing import *
from collections import Counter,defaultdict
from sortedcontainers import SortedList
from functools import cmp_to_key, lru_cache

import sortedcontainers
class Solution1:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter=Counter()
        for i,num in enumerate(nums):
            if num==key and i<=len(nums)-2:
                counter[nums[i+1]]+=1
        return counter.most_common(1)[0] 

class Solution2:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        map={}
        def mapFunc(a):
            nonlocal map
            if a in map:
                return map[a]
            else:
                mappedAVal=0
                strA=str(a)
                exp=1
                for digit in strA[::-1]:
                    mappedAVal+=mapping[int(digit)]*exp
                    exp*=10
                map[a]=mappedAVal
                return mappedAVal

        def compFunc(a,b):
            mappedAVal=mapFunc(a)
            mappedBVal=mapFunc(b)
            return mappedAVal-mappedBVal
        
        nums.sort(key=functools.cmp_to_key(compFunc)) # 记：The built-in sorted() function is guaranteed to be stable.
        return nums


class Solution3: 
    '''
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]: # TLE
        visited=set()
        ancestors=defaultdict(list)
        edges2=defaultdict(list)
        for edge in edges:
            edges2[edge[0]].append(edge[1])

        def dfs(trace,curr):
            visited.add(curr)
            ancestors[curr].extend(trace.copy())   
            for nextV in edges2[curr]:
                trace.append(curr)
                dfs(trace,nextV)
                trace.pop()

        fullSet=set(range(n))
        while len(fullSet-visited)>0:
            dfs( [],tuple(fullSet-visited)[0] )
        
        ret=[]
        for i in range(n):
            ret.append(sorted(set(ancestors[i])))

        return ret
    '''

    ''''''


    '''

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]: # TLE
        revEdges=defaultdict(list)
        visited=set()
        descendents=defaultdict(list)
        for edge in edges:
            revEdges[edge[1]].append(edge[0])

        def dfs(trace):
            curr=trace[-1]
            visited.append(curr)
            for anscestor in trace[:-1]:
                descendents[anscestor].append(curr)
            for nextV in revEdges[curr]:
                if nextV not in visited:
                    trace.append(nextV)
                    dfs(trace)
                    trace.pop()

        fullSet=set(range(n))
        while len(fullSet-visited)>0:
            dfs( [tuple(fullSet-visited)[0]] )
        
        ret=[]
        for i in range(n):
            ret.append(sorted(descendents[i]))

        return ret

    '''

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]: 
        Children=collections.defaultdict(list)
        ancestors=collections.defaultdict(list)
        for edge in edges:
            Children[edge[0]].append(edge[1])
        #    ancestors[edge[1]].append(edge[0])
        
        @lru_cache
        def dfs(s,curr):
            if s!=curr:
                if not ancestors[curr] or s!=ancestors[curr][-1]:
                    ancestors[curr].append(s)
            for child in Children[curr]:
                dfs(s,child)
            #print(s,curr,ancestors)
        for i in range(n):
            dfs(i,i)
        ret=[]
        for i in range(n):
            ret.append(ancestors[i])
        return ret


class Solution4:
    def minMovesToMakePalindrome(self, s: str) -> int:
        if len(s)<=1:
            return 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==s[0]:
                if i==0:
                    return len(s)//2+self.minMovesToMakePalindrome(s[1:])
                else:
                    return len(s)-1-i+self.minMovesToMakePalindrome(s[1:i]+s[i+1:])