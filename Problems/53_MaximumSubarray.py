from typing import List, Tuple
import numpy
'''
#failed
def maxSubIdx(nums: List[int]) -> Tuple[int,int]: # return the start , end index and sum value of maxSubArray
    front=nums[0]
    start=0
    end=0
    
    if len(nums) == 1:
        return start,end,front
    else:
        r_start,r_end,r_sum=maxSubIdx(nums[1:])
        
        if r_start==0: # contiguous
            if front>=0:
                return r_start,r_end+1,r_sum+front
            else:
                return r_start+1,r_end+1,r_sum
        else: # not contiguous
        
        roadsum=0
        #print("rstart:",r_start)
        for i in range(r_start+1):
            roadsum+=nums[i]
        if roadsum>=0:
            return 0,r_end+1,roadsum+r_sum
        else:
            return r_start+1,r_end+1,r_sum
'''
'''
class Solution: #O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        max=float('-inf')
        #print("max:",max)
        prev=0
        for i in range(len(nums)): #i=curr
            if sum(nums[prev:i+1])>max:
                max=sum(nums[prev:i+1])
            if sum(nums[prev:i+1]) <=0:
                i+=1
                prev=i
            else:
                i+=1
        return max
'''
def maxSubIdx(nums: List[int]) -> Tuple[int,int,int]: # return the start , end index and sum value of maxSubArray
    if len(nums) == 1:
        return 0,0,nums[0]
    mid=len(nums)//2
    l_start,l_end,l_max=maxSubIdx(nums[:mid])
    r_start,r_end,r_max=maxSubIdx(nums[mid:])
    if l_max>r_max: # >= makes no difference ?
        lr_max=l_max
        res_start=l_start
        res_end=l_end
    else:
        lr_max=r_max
        res_start=r_start+mid
        res_end=r_end+mid
    converge=sum(nums[l_start:r_end+mid+1])
    if(len(nums))==3:
        print("converge,lrmax:",converge,lr_max)
    if converge<=lr_max: # < makes no difference
        return res_start,res_end,lr_max
    else:
        return l_start,r_end+mid,converge
    
class Solution: #O(log2n)
    def maxSubArray(self, nums: List[int]) -> int:
        start,end,sum=maxSubIdx(nums)
        return sum



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


    
        