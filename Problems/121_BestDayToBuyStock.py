from typing import *
class Solution:
    def maxProfitN2(self, prices: List[int]) -> int: # O(n^2)
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=max(profit,prices[j]-prices[i])
        return profit

    def maxProfit2(self,prices:List[int]) -> int: # faster, but still O(n^2) 
        profit=0
        maxIdx=0
        while True:
            #print("maxidx:",maxIdx)
            if len(prices[maxIdx:])==0:
                maxIdx=len(prices)-1
            else:
                maxIdx=prices.index(max(prices[maxIdx:]),maxIdx)
            
            if len(prices[:maxIdx])==0:
                minIdx=maxIdx
            else:
                minIdx=prices.index(min(prices[:maxIdx]))

            profit=max(profit,prices[maxIdx]-prices[minIdx])
            maxIdx+=1
            if maxIdx>=len(prices):
                break
        return profit

    def maxProfit3(self,prices:List[int]) -> int:
        minIdx=0
        profit=0
        for i in range(len(prices)):
            if prices[i]<prices[minIdx]:
                minIdx=i
            profit=max(profit,prices[i]-prices[minIdx])
        return profit


sol=Solution()
print(sol.maxProfit3([3,3]))

