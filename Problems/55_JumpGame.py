from typing import *
#import sys
class Solution:
    '''
    def canJump(self, nums: List[int]) -> bool: # TLE
        #sys.setrecursionlimit(10000)
        
        if len(nums)==1:
            return True
        
        reached=set()
        def dfs(idx):
            for i in range(nums[idx]):
                if idx+i+1>=len(nums):
                    return
                if idx+i+1 not in reached:
                    reached.add(idx+i+1)
                    dfs(idx+i+1)
        dfs(0)
        return len(nums)-1 in reached
    '''

    def canJump(self, nums: List[int]) -> bool:
        rIdx=len(nums)-1
        for lIdx in range(len(nums)-2,-1,-1):
            if lIdx+nums[lIdx]>=rIdx:
                rIdx=lIdx
        return rIdx==0
