#Map & add -> sub
from typing import *
import numpy
import time
#import Map
def twoSum (nums: List[int], target: int) -> List[int]:
    rlist=list()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            #print("i,j:",i,j)
            if sum==target:
                rlist.append(i)
                rlist.append(j)
                return rlist

def twoSum3(nums: List[int], target: int) -> List[int]:
    diffmap={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in diffmap:
            return [diffmap[diff],i]
        diffmap[nums[i]]=i

r=twoSum3([-3,-1,0,3,4],3)
print(r)
