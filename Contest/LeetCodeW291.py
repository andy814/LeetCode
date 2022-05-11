from functools import cache
from typing import *
from collections import defaultdict
from sortedcontainers import SortedList
class Solution1:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=-1
        for i,ch in enumerate(number):
            if ch==digit:
                cand=number[:i]+number[i+1:]
                ans=max(ans,int(cand))
        return str(ans)

class Solution2:
    def minimumCardPickup(self, cards: List[int]) -> int:
        visited=set()
        ans=float("inf")
        prev=0
        for i,card in enumerate(cards):
            #print("visited:",visited)
            #print("prev,now:",cards[prev],cards[i])
            if card not in visited:
                visited.add(card)
                continue
                
            #if prev==0:
            #    visited.remove(cards[prev])
            #    prev+=1
                
            while cards[prev]!=cards[i]:
                #print("removing:",cards[prev],prev)
                visited.remove(cards[prev])
                prev+=1
            ans=min(ans,i-prev+1)
            prev+=1

        if ans==float("inf"):
            ans=-1
        return ans

class Solution3:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        #divArr=[ 1 for num in nums if num%p==0 else 0]
        divArr=[]
        visited=set()
        for num in nums:
            if num%p==0:
                divArr.append(1)
            else:
                divArr.append(0)
        count=0
        for i in range(1,k+1):
            count+=len(nums)-i+1
        prefix=[]
        curr=0
        for i in range(len(divArr)):
            curr+=divArr[i]
            prefix.append(curr)
        #print("prefix:",prefix)
        
        for i in range(len(nums)):
            if prefix[i]<=k:
                count+=1
                visited.add(tuple(nums[:i+1]))
                
        #print("visited:",visited)
        
        for i in range(1,len(nums)):
            for width in range(1,len(nums)-i+1):
                #print("i,width:",i,width)
                if prefix[i+width-1]-prefix[i-1]<=k:
                    count+=1
                    visited.add(tuple(nums[i:i+width]))
                    #print("accepted")
                    
        #print(visited)
        return len(visited)


class Solution:

    def appealSum(self, s: str) -> int:
        presDict=defaultdict(SortedList)
        for i,ch in enumerate(s):
            presDict[ch].add(i)            
        ans=0
        #print(presDict)
        @cache
        def dp(i):
            if i==0:
                return 1
            else:
                lastAppear=presDict[s[i]].index(i)-1
                #print("curr,lastAppear:",s[i],presDict[s[i]][lastAppear])
                ret=dp(i-1)+i-(presDict[s[i]][lastAppear]) if lastAppear>=0 else dp(i-1)+i+1
                return ret
        for i in range(len(s)):
            #print(dp(i))
            ans+=dp(i)
        return ans
        

    def appealSum(self, s: str) -> int: # another method, simpler
        ans=0
        prev=defaultdict(lambda:-1)
        for i in range(len(s)):
            ans+=(i-prev[s[i]])*(len(s)-i)
            prev[s[i]]=i
        return ans