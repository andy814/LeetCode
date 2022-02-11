from typing import *
class Solution2:
    def search(self, nums: List[int], target: int) -> int: # O(n)
        return nums.index(target) if target in nums else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int: # O(logn)
        if len(nums)==1:
            return 0 if nums[0]==target else -1 
        pivot=-1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(end+start)//2
            if mid+1<len(nums):
                if nums[mid]>nums[mid+1]:
                    pivot=mid
                    break
            if end+1<len(nums):
                if nums[end]>nums[end+1]:
                    pivot=end
                    break
            if start-1>=0:
                if nums[start-1]>nums[start]:
                    pivot=start-1
                    break
            if nums[mid]>nums[end]:
                start=mid+1
            elif nums[start]>nums[mid]:
                end=mid-1
            else:
                break # pivot=-1
        start=0
        end=len(nums)-1
        n=len(nums)
        while start<=end: # 4 5 6 7 0 1 2 pivot=3
            mid=(end+start)//2
            if nums[(mid+pivot+1)%n]<target:
                start=mid+1
            elif nums[(mid+pivot+1)%n]>target:
                end=mid-1
            else:
                return (mid+pivot+1)%n
        return -1