from typing import *
from collections import Counter
from functools import cache
class Solution1:
    def percentageLetter(self, s: str, letter: str) -> int:
        counter=Counter(s)
        if letter not in counter:
            return 0
        else:
            return counter[letter]*100//len(s)

class Solution2:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff=[]
        for i in range(len(rocks)):
            diff.append(capacity[i]-rocks[i])
        diff.sort()
        currSum=0
        i=0
        for num in diff:
            currSum+=num
            if currSum>additionalRocks:
                break
            i+=1
        return i

import fractions
fractions.Fraction()
class Solution: # mark
    def minimumLines(self, stockPrices: List[List[int]]) -> int: # ERROR
        if len(stockPrices)==1:
            return 0
        elif len(stockPrices)==2:
            return 1
        eps=10**(-50)
        stockPrices.sort()
        lines=len(stockPrices)-1
        for i in range(1,len(stockPrices)-1):
            prevD=(stockPrices[i][1]-stockPrices[i-1][1])/(stockPrices[i][0]-stockPrices[i-1][0])
            nextD=(stockPrices[i+1][1]-stockPrices[i][1])/(stockPrices[i+1][0]-stockPrices[i][0])
            print(prevD,nextD)
            if nextD-eps<=prevD<=nextD+eps:
                lines-=1
        return lines

    def minimumLines(self, stockPrices: List[List[int]]) -> int: # Solution 1: cross product
        import numpy as np

        if len(stockPrices)==1:
            return 0
        elif len(stockPrices)==2:
            return 1

        eps=10**(-50)
        stockPrices.sort()
        lines=len(stockPrices)-1
        
        @cache
        def cross(v1,v2):
            return np.cross(v1,v2)
        
        for i in range(1,len(stockPrices)-1):
            prevD=(stockPrices[i][1]-stockPrices[i-1][1],stockPrices[i][0]-stockPrices[i-1][0])
            nextD=(stockPrices[i+1][1]-stockPrices[i][1],stockPrices[i+1][0]-stockPrices[i][0])
            if cross(prevD,nextD)==0:
                lines-=1
        return lines
    
    def minimumLines(self, stockPrices: List[List[int]]) -> int: # Solution 2: fractions
        import fractions
        if len(stockPrices)==1:
            return 0
        elif len(stockPrices)==2:
            return 1
        stockPrices.sort()
        lines=len(stockPrices)-1
        for i in range(1,len(stockPrices)-1):
            prevD=fractions.Fraction(stockPrices[i][1]-stockPrices[i-1][1],stockPrices[i][0]-stockPrices[i-1][0])
            nextD=fractions.Fraction(stockPrices[i+1][1]-stockPrices[i][1],stockPrices[i+1][0]-stockPrices[i][0])
            print(prevD,nextD)
            if prevD==nextD:
                lines-=1
        return lines

    def minimumLines(self, stockPrices: List[List[int]]) -> int: # Solution 3: convert division to multiplication
        if len(stockPrices)==1:
            return 0
        elif len(stockPrices)==2:
            return 1
        eps=10**(-50)
        stockPrices.sort()
        lines=len(stockPrices)-1
        for i in range(1,len(stockPrices)-1):
            y2y1=stockPrices[i][1]-stockPrices[i-1][1]
            x2x1=stockPrices[i][0]-stockPrices[i-1][0]
            y3y2=stockPrices[i+1][1]-stockPrices[i][1]
            x3x2=stockPrices[i+1][0]-stockPrices[i][0]
            #print(prevD,nextD)
            if y2y1*x3x2==x2x1*y3y2:
                lines-=1
        return lines




class Solution:
    def totalStrength(self, strength: List[int]) -> int: # O(n^3),horrible
        def calcInterval(a,b):
            weakest=min(strength[a:b+1])
            sumP=sum(strength[a:b+1])
            return weakest*sumP
        mod=10**9+7
        total=0
        for i in range(len(strength)):
            for j in range(i,len(strength)):
                total+=calcInterval(i,j)%mod
        return total%mod


#https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2062017/C%2B%2B-prefix-%2B-monotonic-stack-O(N)-solution-with-thought-process
# 正确性证明：1.该算法找到的区间互不重复 2. 每个子数组区间都得到了统计，即不存在未被该算法统计的区间
# 也可以证明单射+满射。令A为用[start,end]定义的所有区间集合，B为pivot法找到的区间集合。注意pivot法找到的区间互相不会重复，符合集合定义
# 满射：对于任何一个pivot法找到的区间，都存在[start,end]，即在A中存在原相。
# 单射：对于任意两个[start,end]定义下不同的区间，它们在pivot法中对应的区间一定不同。


class Solution: 
