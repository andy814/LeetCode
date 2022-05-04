from typing import *
from collections import Counter
import heapq
from functools import cache
class Solution1:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter()
        for num in nums:
            count[num]+=1
        for num in count:
            if count[num]&1:
                return False
        return True

class Solution2:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0]==pattern[1]:
            count0=text.count(pattern[0])
            return count0*(count0+1)//2
        count=Counter()
        sumSubSeq=0
        for char in text:
            count[char]+=1
            if char==pattern[1]:
                sumSubSeq+=count[pattern[0]]
        return sumSubSeq+max(count[pattern[0]],count[pattern[1]])

class Solution3:
    def halveArray(self, nums: List[int]) -> int:
        oldNumSum=sum(nums)
        numSum=oldNumSum
        count=0
        nums=[num*-1 for num in nums]
        heapq.heapify(nums)
        while numSum*2>oldNumSum:
            count+=1
            top=heapq.heappop(nums)*-1
            top/=2
            numSum-=top
            heapq.heappush(nums,top*-1)
        return count



class FenwickTree():
    def __init__(self, N=0):
        self.N = N
        self.bit = [0 for i in range(N+1)]

    def construct(self,aa):
        self.N=len(aa)
        self.bit=[0 for i in range(self.N+1)]
        for i,num in enumerate(aa):
            self.add(i,num)


    def add(self, index, value):
        index += 1
        while index <= self.N:
            self.bit[index] += value
            index += (index & -index)

    def prefixSum(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans += self.bit[index]
            index -= (index & -index)
        return ans

    def print(self):
        print(self.bit)

    def query(self,start,end): # return the sum of [start,end)
        return self.prefixSum(end-1)-self.prefixSum(start-1)

class Solution4:
    '''
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int: # TLE
        floor=[int(f) for f in floor] 
        BIT=FenwickTree(len(floor))
        BIT.construct(floor)
        def dp(i,BIT,carpetsLeft):
            if i>=BIT.N or carpetsLeft==0:
                return BIT.query(0,BIT.N)
            else:
                top=min(BIT.N,i+carpetLen)
                addMap=set()
                for j in range(i,top): # turn white into black
                    if BIT.query(j,j+1)==1:
                        addMap.add(j)
                for j in addMap:
                    BIT.add(j,-1)
                dp1=dp(top,BIT,carpetsLeft-1)
                for j in addMap:
                    BIT.add(j,1)
                dp2=dp(i+1,BIT,carpetsLeft)
            return min(dp1,dp2)
        return dp(0,BIT,numCarpets)
    '''

    '''
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int: # TLE
        floor=[int(f) for f in floor]
        BIT=FenwickTree(len(floor))
        BIT.construct(floor)
        
        sumCounter={}
        for i in range(0,BIT.N-carpetLen+1):
            sumCounter[i]=BIT.query(i,i+carpetLen)
        
        while numCarpets>0 and BIT.query(0,BIT.N)>0:
            numCarpets-=1
            maxNbr,maxIdx=-1,-1
            for i in range(0,BIT.N-carpetLen+1):
                if BIT.query(i,i+carpetLen)>maxNbr:
                    maxNbr=BIT.query(i,i+carpetLen)
                    maxIdx=i
        
            for i in range(maxIdx,maxIdx+carpetLen):
                if BIT.query(i,i+1)==1:
                    BIT.add(i,-1)
        
        return BIT.query(0,BIT.N)
    '''    

    def minimumWhiteTiles(self, floor, k, L):
        @cache
        def dp(i,k):
            if k<0:
                return float("inf")
            if i>=len(floor):
                return 0
            ret=min( dp(i+1,k)+int(floor[i]=="1"), dp(i+L,k-1) )
            return ret
        return dp(0,k)