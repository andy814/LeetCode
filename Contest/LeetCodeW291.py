from typing import *

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
        prev=0
        visited=set()
        ans=0
        for i,curr in enumerate(s):
            
            print("curr,visited:",curr,visited)
            if curr not in visited:
                visited.add(curr)
                continue
                
            lenV=len(visited)
            ans+=lenV*(lenV+1)//2
            print("ans:",ans)
            #prev+=1

            while s[prev]!=s[i]:
                visited.remove(s[prev])
                prev+=1
            prev+=1

        lenV=len(visited)
        ans+=lenV*(lenV+1)//2
        #prev+=1
            
        return ans