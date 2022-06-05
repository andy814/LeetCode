from typing import *
import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # TLE
        @functools.cache
        def dp(i,target):
            if target<0:
                return float("inf")
            elif target==0:
                return 0
            if i==-1: # target > 0 here
                return float("inf")
            
            ans=float("inf")
            for coin in coins:
                num=0
                while coin*num<=target:
                    cand=num+dp(i-1,target-coin*num)
                    ans=min(ans,cand)
                    num+=1
            return ans
        ans=dp(len(coins)-1,amount)
        if ans==float("inf"):
            return -1
        else:
            return ans

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(len(dp)):
            for coin in coins:
                if i>=coin:
                    cand=dp[i-coin]+1
                    dp[i]=min(dp[i],cand)
        dp[-1]=-1 if dp[-1]==float("inf") else dp[-1]
        return dp[-1]
            
