from typing import *
import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k>=len(nums)+1:
            return True
        if t==0:
            countSet=set()
            for i,num in enumerate(nums):
                if i>k:
                    countSet.remove(nums[i-k-1])
                if num in countSet:
                    return True    
                countSet.add(num)
            return False


        aa={}
        for i,num in enumerate(nums):
            #print(aa)
            if (num//t) in aa:
                #print("1")
                return True
            elif (num//t)-1 in aa:
                if num-aa[(num//t)-1]<=t:
                    #print("2")
                    return True
            elif (num//t)+1 in aa:
                if aa[(num//t)+1]-num<=t:
                    #print("3")
                    return True
            aa[num//t]=num
            if i>=k and nums[i-k]//t in aa:
                aa.pop(nums[i-k]//t)
        return False
            


        