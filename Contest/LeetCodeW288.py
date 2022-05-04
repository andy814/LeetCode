from shutil import move
from typing import *
from collections import defaultdict
from collections import deque
from functools import cache
from collections import Counter
import bisect


class Solution1:
    def largestInteger(self, num: int) -> int:
        odds=[]
        evens=[]
        ret=[]

        strnum=str(num)
        for n in strnum:
            if int(n)%2==0:
                evens.append(int(n))
            else:
                odds.append(int(n))

        odds.sort(reverse=True) #int
        evens.sort(reverse=True)

        oddPtr=0
        evenPtr=0
        for n in strnum:
            if int(n) in odds:
                ret.append(odds[oddPtr])
                oddPtr+=1
            else:
                ret.append(evens[evenPtr])
                evenPtr+=1
        
        strret=""
        for num in ret:
            strret+=str(num)
        return int(strret)


class Solution2:
    def minimizeResult(self, expression: str) -> str:
        splits=expression.split("+")
        a=int(splits[0])
        b=int(splits[1])
        ans=a+b
        stra=str(a)
        strb=str(b)
        for i in len(stra-1):
            for j in len(strb-1):
                Lmult=int(stra[:i])
                Ladd=int(stra[i:])
                Radd=int(strb[:j])
                Rmult=int(strb[j:])
                ans=min(ans,Lmult*Rmult*(Ladd+Radd))

class Solution3:    
    def maximumProduct(self, nums: List[int], k: int) -> int:
        numCounter=Counter()
        for num in nums:
            numCounter[num]+=1
        nums.sort()

        for num in nums:
            if k<=0:
                break
            add=min(k,numCounter[num])
            k-=add
            numCounter[num]-=add
            numCounter[num+1]+=add
        
        prod=1
        for num in numCounter:
            prod*=numCounter[num]
        return prod

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        
        flowers=[min(f,target) for f in flowers]
        if newFlowers>=len(flowers)*target-sum(flowers):
            #print(full*(len(flowers)-1)+partial*(target-1))
            return max( full*len(flowers), full*(len(flowers)-1)+partial*(target-1) )
        
        flowers.sort()
        cost=[0]
        for idx in range(1,len(flowers)):
            cost.append( cost[-1] + (idx)*(flowers[idx]-flowers[idx-1]) )
            
            
        #print(cost)
        ans=0
        currIdx=len(flowers)-1 # the right of currIdx are complete gardens
        while newFlowers>0:
            if flowers[currIdx]==target:
                currIdx-=1
                continue
            if cost[currIdx]>newFlowers:
                insertIdx=bisect.bisect_right(cost,newFlowers)-1
            else:
                insertIdx=currIdx
            #insertIdx = min(currIdx, bisect_right(cost, newFlowers) - 1)
            #insertIdx=bisect.bisect_right(cost,newFlowers)
            incompleteMin=flowers[insertIdx] + (newFlowers-cost[insertIdx])//(insertIdx+1)
            ans=max( ans, partial*incompleteMin + full*(len(flowers)-currIdx-1) )
            newFlowers-=target-flowers[currIdx]
            currIdx-=1

        return ans
            

            
