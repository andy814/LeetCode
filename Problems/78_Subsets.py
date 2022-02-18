from typing import *
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret=[nums]
        for i in range(len(nums)):
            ret.extend( [list(comb) for comb in itertools.combinations(nums,i)] )
        return ret

    def subsets_backtrace(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret=[[]]
        def dfs(start,trace):
            trace.append(nums[start])
            ret.append(trace[:])
            for i in range(start+1,len(nums)):
                dfs(i,trace)
            trace.pop(-1)


        dfs(0,[])
        return ret