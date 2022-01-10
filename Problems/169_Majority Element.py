import collections
from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int: # space:O(n), 15.6MB
        counts=collections.defaultdict(lambda:0)
        for i in nums:
            counts[i]+=1
        for i in counts:
            if counts[i]>len(nums)//2:
                return i
                
    def majorityElementVote(self, nums: List[int]) -> int: #space:O(1), 15.6MB, but the percentile differs from 10% to 90%
        count=0
        major=None
        for num in nums:
            if major==None:
                major=num
                count+=1
                continue
            if num==major:
                count+=1
            else:
                count-=1
                if count==0:
                    major=None
        return major
            