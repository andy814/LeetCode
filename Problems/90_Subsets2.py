from itertools import combinations
from typing import *
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        for i in range(len(nums)+1):
            comb=combinations(nums,i)
            combSet=set([tuple(sorted(c)) for c in comb])
            ans=[ list(c) for c in combSet] # anstype:list[list]
            ret.extend(ans)
        return ret

    def subsetsWithDup_recur(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        nums.sort()
        def dfs(track,start):
            ret.append(track[:])
            for i in range(start,len(nums)):
                if i==0 or nums[i]!=nums[i-1]:
                    track.append(nums[i])
                    dfs(track,i+1)
                    track.pop()
        
        dfs([],0)
        return ret
