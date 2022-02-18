from typing import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr0=-1
        ptr1=-1
        ptr2=0
        while ptr2<len(nums):

            if nums[ptr2]==2:
                pass
            elif nums[ptr2]==1:
                ptr1+=1
                nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
            else:
                ptr0+=1
                nums[ptr0],nums[ptr2]=nums[ptr2],nums[ptr0]
                ptr1+=1
                nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
            ptr2+=1
        