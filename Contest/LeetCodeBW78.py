from typing import *
from collections import Counter
import heapq
from functools import cache
from itertools import combinations
import collections
from nose import run_exit
from sortedcollections import SortedList
from collections import deque
import bisect

class Solution1:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numstr=str(num)
        length=len(str(num))
        count=0
        for i in range(length-k+1):
            if num%int(numstr[i:i+k])==0:
                count+=1
        return count

class Solution2:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum=0
        rightSum=sum(nums)
        count=0
        i=0
        while i<len(nums)-1:
            leftSum+=nums[i]
            rightSum-=nums[i]
            if leftSum>=rightSum:
                count+=1
            i+=1
        return count

class Solution3:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        lengths= [ (tile[1]-tile[0]+1) for tile in tiles ]
        starts= [tile[0] for tile in tiles]
        ends= [tile[1] for tile in tiles]
        prefixs=[]
        
        prefixSum=0
        for length in lengths:
            prefixSum+=length
            prefixs.append(prefixSum)
            
        ans=0
        for i,tile in enumerate(tiles):
            carpetStart=tile[0]
            carpetEnd=carpetStart+carpetLen
            targetIdx=bisect.bisect_left(ends,carpetEnd) 
            if targetIdx>=len(tiles):
                if i==0:
                    return prefixs[-1]
                covered=prefixs[-1]-prefixs[i-1]
                ans=max(ans,covered)
                continue
                
            targetTile=tiles[targetIdx]
            covered=0
            if i==0:
                covered+=prefixs[targetIdx-1]
            else:
                covered+=prefixs[targetIdx-1]-prefixs[i-1]

            if targetTile[0]<carpetEnd:
                covered+=carpetEnd-targetTile[0]

            ans=max(ans,covered)
        return ans

class Solution4:
    def largestVariance(self, s: str) -> int: # O(n^2)
        ans=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                c=collections.Counter(s[i:j+1])
                ans=max(ans,c.most_common()[0][1]-c.most_common()[-1][1])
        return ans

    def largestVariance(self, s: str) -> int: # O(n^2)
        def kadane(arr):
            ans=-float("inf")
            currSum=0
            for num in arr:
                currSum+=num
                ans=max(currSum,ans)
                if currSum<0:
                    currSum=0
            return ans

        ans=0
        letters=list(set(s))
        for ch1 in letters:
            for ch2 in letters:
                if ch1==ch2:
                    continue
                temp=s.replace("1",ch1)
                temp=temp.replace("2",ch2)
                tempArr=[]
                for ch in temp:
                    if ch=="2":
                        tempArr.append(1)
                    elif ch=="1":
                        tempArr.append(-1)
                    else:
                        tempArr.append(0)
                        
                ans=max(ans,kadane(tempArr))
        return ans


                


