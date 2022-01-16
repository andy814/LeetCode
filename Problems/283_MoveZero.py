from typing import *
class Solution:
    def moveZeroes(self, nums: List[int]) -> None: #O(n^2)
        ptr=0
        count=0
        while ptr<len(nums):
            if nums[ptr]!=0:
                ptr+=1
                count=0
            else:
                for i in range(ptr,len(nums)-1):
                    nums[i]=nums[i+1]
                nums[-1]=0
                count+=1
                if count>len(nums)-ptr:
                    return

    def moveZeroes2(self, nums: List[int]) -> None: #O(n)
        ptr=0
        zeroLen=0
        while ptr<len(nums):
            if nums[ptr]==0:
                ptr+=1
                zeroLen+=1
            else:
                nums[ptr],nums[ptr-zeroLen]=nums[ptr-zeroLen],nums[ptr]
                ptr+=1
sol=Solution()
sol.moveZeroes([0,1,0,3,12])

        
