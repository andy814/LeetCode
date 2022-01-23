import collections
from typing import *
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool: # O(n^2),time limit exceeded
        metRev=collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    metRev[i].append(j)
                    metRev[j].append(i)
        revCount=0
        maxRev=0
        for key in metRev:
            revCount+=len(metRev[key])
            if len(metRev[key])>maxRev:
                maxRev=len(metRev[key])
        if revCount-2*maxRev>0:
            return False
        else:
            return True
    
    def checkPossibility2(self, nums: List[int]) -> bool: # O(n^2),time limit exceeded
        sortedNums=nums.sort()
        while 
        metRev=collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    metRev[i].append(j)
                    metRev[j].append(i)
        revCount=0
        maxRev=0
        for key in metRev:
            revCount+=len(metRev[key])
            if len(metRev[key])>maxRev:
                maxRev=len(metRev[key])
        if revCount-2*maxRev>0:
            return False
        else:
            return True
