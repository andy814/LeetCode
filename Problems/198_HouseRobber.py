from typing import *



class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robDP(nums)

    '''
    def robDP(self,nums): # TimeLimitExceeded
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]

        return max(self.robDP(nums[1:]),nums[0]+self.robDP(nums[2:]))
    '''

    def robDP(self,nums): #space: O(n)
        
        if len(nums)==1:
            return nums[0]
        
        visit=[0]*len(nums)

        visit[len(nums)-1]=nums[-1]
        visit[len(nums)-2]=max(nums[-1],nums[-2])

        for i in range(len(nums)-3,-1,-1):
            visit[i]=max( visit[i+1], nums[i]+visit[i+2] )

        return visit[0]

    def robDP2(self,nums): #space: O(1)
        
        if len(nums)==1:
            return nums[0]

        iP2=nums[-1]
        iP1=max(nums[-1],nums[-2])

        for i in range(len(nums)-3,-1,-1):
            iP0=max(iP1,nums[i]+iP2)
            iP2=iP1
            iP1=iP0

        return iP1