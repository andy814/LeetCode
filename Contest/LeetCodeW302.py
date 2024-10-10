from typing import *
from sortedcontainers import SortedList
from collections import Counter,defaultdict
from functools import cache
from collections import deque
from math import comb
import numpy as np
import math
import functools
from sympy import fraction

class Solution1:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ctr=Counter(nums)
        for key in ctr:
            ctr[key]=ctr[key]%2
        left=sum(ctr[key] for key in ctr)
        return [(len(nums)-left)//2,left]

class Solution2:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num):
            ans=0
            for ch in str(num):
                ans+=int(ch)
            return ans
        sumList=defaultdict(list)
        for num in nums:
            sumList[digitSum(num)].append(num)
        for key in sumList:
            sumList[key].sort(reverse=True)
        ans=-1
        for key in sumList:
            if len(sumList[key])>2:
                ans=max(ans,sumList[key][0]+sumList[key][1])
        return ans

# time:
# sort:100*100log100
# query: 100*100

# space: 100*100*100*2


# check the answers
import numpy as np
import fractions
import time
class Solution3_1: # TLE
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        trimmedNums=[[]]
        sigma=10**-7
        time1=time.time()
        for i in range(1,len(nums[0])+1): # 100
            trimmedNums.append([])
            temp=[fractions.Fraction(num[-i:]) for num in nums] # 10^4 in total
            visitSet=set()
            for num in temp: # 100
                if num in visitSet:
                   num+=sigma
                   sigma+=10**-7
                trimmedNums[i].append(num)
                visitSet.add(num)
        sortedTrimmedNums=[]
        time2=time.time()
        for i in range(len(trimmedNums)):
            print(len(trimmedNums[i]))
            trimmedNums[i]=np.argsort(trimmedNums[i],kind="mergesort")
        time3=time.time()
        ans=[]
        for query in queries:
            k,trim=query[0],query[1]
            targetIdx=trimmedNums[trim][k-1]
            ans.append(targetIdx)
        time4=time.time()
        print(time2-time1)
        print(time3-time2)
        print(time4-time3)
        return ans

import numpy as np
import time
class Solution3_2:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        time1=time.time()
        trimmedNums=defaultdict(list)
        for num in nums: # 100
            curr=0
            for i,ch in enumerate(num[::-1]): # 100
                curr+=int(ch)*10**i
                trimmedNums[i+1].append(curr)   
        time2=time.time()
        for key in trimmedNums: # 100* 100log100
            trimmedNums[key]=np.argsort(trimmedNums[key],kind="mergesort")
        time3=time.time()
        ans=[]
        for query in queries:
            k,trim=query[0],query[1]
            targetIdx=trimmedNums[trim][k-1]
            ans.append(targetIdx)
        time4=time.time()
        print(time2-time1)
        print(time3-time2)
        print(time4-time3)
        return ans

class Solution3_3:
    def smallestTrimmedNumbers(self, A: List[str], queries: List[List[int]]) -> List[int]:  
        def solve(top, pos):
            a = []
            for num in A: # 100
                a.append(int(num[l-pos:]))
            for i in range(len(a)):
                a[i] = (a[i],i)
            a.sort() # 100*log100
            return a[top-1][1]
        res = [] 
        l = len(A[0])
        for top,pos in queries:
            res.append(solve(top,pos)) # 100* T(solve)
        return res

class Solution4_1: # I dont understand why this one will pass.
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        ctr=Counter(nums)
        toDelete=0
        #numsDivide.sort()
        for key in ctr:
            flag=True
            for div in numsDivide:
                if div%key!=0:
                    flag=False
                    toDelete+=ctr[key]
                    break
            if flag:
                return toDelete
        return -1

class Solution4_2:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g=functools.reduce(math.gcd,nums)
        small=float("inf")
        for num in nums:
            if g%num==0:
                small=min(small,num)
        if small==float("inf"):
            return -1
        ans=0
        for num in nums:
            if num<small:
                ans+=1
        return ans
                    