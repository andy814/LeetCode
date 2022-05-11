from typing import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=max(nums)
        
        def dp(i): #return:min,max
            if i==0:
                return nums[0],nums[0]
            prev_min,prev_max=dp(i-1)
            curr_min=min(prev_min*nums[i],prev_max*nums[i],nums[i])
            curr_max=max(prev_min*nums[i],prev_max*nums[i],nums[i])
            return curr_min,curr_max

        return dp(len(nums)-1)[0]

    