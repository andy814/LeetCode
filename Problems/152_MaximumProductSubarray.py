from typing import *
class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     ans=max(nums)
    #     absNums=[abs(n) for n in nums]
    #     prev=0
    #     product=1
    #     for i in range(len(nums)-1):
    #         product*=nums[i]
    #         ans=max(ans,product)
    #         if 0<=nums[i+1]<=1:
    #             while prev<i:
    #                 product/=nums[prev]
    #                 ans=max(ans,product)
    #                 prev+=1
    #     return ans   
    def maxProduct(self, nums: List[int]) -> int:
        def dp(i):
            if i>=len(nums):
                return 1
            else:
                return max(nums[i]*dp(i+1),dp(i+1))
        return dp(0)


