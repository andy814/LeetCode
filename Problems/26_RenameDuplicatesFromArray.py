#Fast-Slow Pointer
from typing import List

class Solution:

    def merge(self,nums,prev,curr):
        distance=len(nums)-curr
        for i in range(1,distance):
            nums[prev+i]=nums[curr+i]
    
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #k=len(nums) #return value
        curr=1
        prev=0
        while curr<len(nums):
            if nums[curr] == nums[prev]:
                curr+=1
            else:
                prev+=1
                nums[prev]=nums[curr]
                curr+=1
        return prev+1
           

    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=len(nums) #return value
        curr=0
        prev=0
        while curr<k:
            while nums[curr] == nums[prev]:
                print("curr:",curr)
                print("prev:",prev)
                #print("currnum:",nums[curr])
                #print("prevnum",nums[prev])
                print("k:",k)
                curr+=1
                if curr==k:
                    break
            if curr != prev:
                curr-=1
                k-=curr-prev
                self.merge(nums,prev,curr)
            prev+=1
            curr=prev
        return k
    '''
        
aa=[]
k=Solution().removeDuplicates(aa)
print(k,aa)