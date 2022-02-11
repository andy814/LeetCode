from typing import *
class Solution2:
    def search(self, nums: List[int], target: int) -> int: # O(n)
        return nums.index(target) if target in nums else -1

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int: # O(logn)
        if len(nums)==1:
            return 0 if nums[0]==target else -1 

        if len(nums)==2:
            if target in nums:
                return 0 if nums[0]==target else 1
            else:
                return -1
        
        start=len(nums)//2
        end=len(nums)-1
        pivot=-1  # 4 5 6 7 0 1 2 pivot=3
        
        # front search
        while start<=end:
            mid=(end+start)//2 # 1 2 4 5 6 7 0
            print("start,end,mid:",start,end,mid)
            if nums[mid]>nums[start]:
                start=mid+1
            elif nums[mid]==nums[start]:
                if mid+1<len(nums):
                    pivot=mid if nums[mid]>nums[mid+1] else -1
                else:
                    pivot=-1
                break
            else:
                end=mid-1

        print("-----------")
        # back search
        if pivot==-1:
            start=0
            end=len(nums)//2
            while start<=end:
                mid=(end+start)//2
                print("start,end,mid:",start,end,mid)
                if nums[mid]>nums[end]: # 5 6 7 0 1 2 4 
                    start=mid+1
                elif nums[mid]==nums[end]:
                    if mid+1<len(nums):
                        pivot=mid if nums[mid]>nums[mid+1] else -1
                    else:
                        pivot=-1
                    break
                else: # 7 0 1 2 4 5 6
                    end=mid-1
            
        # offset=(i-pivot-1)%n
        start=0
        end=len(nums)-1
        n=len(nums)
        print("pivot:",pivot)

        while start<=end: # 4 5 6 7 0 1 2 pivot=3
            mid=(end+start)//2
            print("start,end,mid:",start,end,mid)
            print("searching:",(mid-pivot-1)%n)
            if nums[(mid+pivot+1)%n]<target:
                start=mid+1
            elif nums[(mid+pivot+1)%n]>target:
                end=mid-1
            else:
                return (mid+pivot+1)%n
        return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int: # O(logn)
        if len(nums)==1:
            return 0 if nums[0]==target else -1 
        pivot=-1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(end+start)//2
            #print("start,end,mid:",start,end,mid)

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
        #print("pivot:",pivot)

        while start<=end: # 4 5 6 7 0 1 2 pivot=3
            mid=(end+start)//2
            #print("start,end,mid:",start,end,mid)
            #print("searching:",(mid-pivot-1)%n)
            if nums[(mid+pivot+1)%n]<target:
                start=mid+1
            elif nums[(mid+pivot+1)%n]>target:
                end=mid-1
            else:
                return (mid+pivot+1)%n
        return -1

sol=Solution()
print(sol.search([5,1,3],3))
