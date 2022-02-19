from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums
        curr=1
        prev=1
        count=1
        processingNbr=nums[0]
        while curr<len(nums):
            if nums[curr]==processingNbr:
                count+=1
                if count<=2:
                    prev+=1
                curr+=1
            else:
                count=1
                processingNbr=nums[curr]
                curr+=1
                prev+=1
            if prev!=curr:
                nums[curr-1],nums[prev-1]=nums[prev-1],nums[curr-1]
        return nums