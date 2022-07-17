from copy import deepcopy
import functools
from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations
import collections
from matplotlib.style import available
from nose import run_exit
from sortedcollections import SortedList
from collections import deque
import bisect
import math

from sympy import evaluate

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluateRoot(root):
            if not root.left:
                return root.val
            else:
                L=evaluateRoot(root.left)
                R=evaluateRoot(root.right)
                if root.val==2:
                    return 0 if L+R==0 else 1
                elif root.val==3: # AND
                    return 1 if L+R==2 else 0

        rootVal=evaluateRoot(root)
        if rootVal==1:
            return True
        else:
            return False

class Solution2:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        
        buses.sort()
        passengers.sort()
        rev_passengers=dict((p,i) for i,p in enumerate(passengers))
        #print(rev_passengers)
        
        leftAvailableTime=dict() # key: passenger index  value: latest available time slot before this guy
        arriveSet=set(passengers)
        for i,passenger in enumerate(passengers):
            if i==0:
                leftAvailableTime[i]=passenger-1
                continue
            if passenger-1 in arriveSet:
                leftAvailableTime[i]=leftAvailableTime[i-1]
            else:
                leftAvailableTime[i]=passenger-1

        leave=0
        ans=1
        #print(leftAvailableTime)
        
        for i,bus in enumerate(buses):
            can_carry=bisect.bisect_right(passengers,bus)
            carry=min(capacity,can_carry-leave)
            lastPassenger=leave+carry-1
            #print(i,carry,lastPassenger)         
            if carry>=capacity:
                ans=max(ans,leftAvailableTime[lastPassenger])
            else:
                if bus in rev_passengers:
                    ans=max(ans,leftAvailableTime[rev_passengers[bus]])
                else:
                    ans=max(ans,bus)
            leave+=carry
        return ans

class Solution2: # elegant
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passengerSet=set(passengers)
        passengerIdx=0
        for bus in buses:
            cap=capacity
            while cap and passengerIdx<len(passengers) and passengers[passengerIdx]<=bus:
                cap-=1
                passengerIdx+=1
        
        if cap:
            ans=buses[-1]
        else:
            ans=passengers[passengerIdx-1]
        while ans in passengerSet:
            ans-=1
        return ans 



class Solution3:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff= [abs(num1-num2) for (num1,num2) in zip(nums1,nums2)]
        diffSum=sum(diff)
        k=k1+k2
        if k>=diffSum:
            return 0
        diff.sort(reverse=True)
        prefixSum=[]
        currSum=0
        for nbr in diff:
            currSum+=nbr
            prefixSum.append(currSum)
        
        temp=0
        idx=0
        while idx<len(diff)-1 and (prefixSum[idx]-k)//(idx+1)<diff[idx+1]:
            idx+=1
            
        div=(prefixSum[idx]) // (idx+1)
        residual=(prefixSum[idx])% (idx+1)
        for i in range(idx):
            diff[idx]=div
        for i in range(residual):
            diff[i]+=1
            
        newDiff=[div]*len(diff)
        for i in range(residual):
            newDiff[i]+=1
        ans=0
        for d in newDiff:
            ans+=d**2
        print(newDiff)
        return ans