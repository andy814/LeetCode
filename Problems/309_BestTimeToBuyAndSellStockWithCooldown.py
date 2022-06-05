from typing import *
import functools
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @functools.cache
        def dp(i,hasHold):
            if i>=len(prices):
                return 0
            if hasHold:
                sell=prices[i]+dp(i+2,False)
                wait=dp(i+1,True)
                return max(sell,wait)
            else:
                buy=-prices[i]+dp(i+1,True)
                wait=dp(i+1,False)
                return max(buy,wait)
        return dp(0,0)