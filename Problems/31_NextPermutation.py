from typing import *
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        swapidx=-1
        for i in range(len(nums)-2,-1,-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    swapidx=i
                    break
            if swapidx!=-1:
                break
        if swapidx!=-1:
            nums[swapidx+1:]=sorted(nums[swapidx+1:])
        else:
            nums.reverse()
