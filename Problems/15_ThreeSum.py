from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        diff={-num for num in nums}
        ret=set({})
        for sumNbr in diff:
            subSet=set({})
            numsLeft=nums[:]
            numsLeft.remove(-sumNbr)
            for num in numsLeft:
                diffNbr=sumNbr-num
                if num in subSet:
                    ret.add(tuple(sorted([-sumNbr,num,diffNbr])))
                subSet.add(diffNbr)
        return list(ret)