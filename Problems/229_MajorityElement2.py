from typing import *
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter=collections.Counter(nums)
        ret=[]
        for key in counter:
            if counter[key]>len(nums)//3:
                ret.append(key)
        return ret