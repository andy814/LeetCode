from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp=[]
        for num in nums:
            if num not in temp:
                temp.append(num)
            elif num in temp:
                temp.remove(num)
        return temp[0]

    def fasterSingleNumber(self, nums: List[int]) -> int:
        ret=0
        for num in nums:
            ret^=num
        return ret

