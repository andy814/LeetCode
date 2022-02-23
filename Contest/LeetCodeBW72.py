from typing import *
import collections
class Solution1:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        return count

class Solution2:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3==0:
            return 
        mid=num//3
        return [mid-1,mid,mid+1]

class Solution3:
    '''
    def maximumEvenSplit(self, finalSum: int) -> List[int]: #TLE
        ret=[]
        def dfs(track,start,currSum): # track: viewed; currSum: trackSum
            if currSum==finalSum:
                if len(track)>len(ret):
                    ret=track
            elif currSum>finalSum:
                return
            for i in range(start,finalSum,2):
                track.append(i)
                dfs(track,i+2,currSum+i)
                track.pop()
        dfs([],2,0)
        return ret
    '''

    def maximumEvenSplit(self, finalSum: int) -> List[int]: #TLE
        if finalSum&1:
            return []
        finalSum//=2
        currSum=0
        ret=[]
        for i in range(1,finalSum):
            currSum+=i
            ret.append(i)
            if currSum==finalSum:
                return [num*2 for num in ret]
            if currSum>finalSum:
                ret[-1]=finalSum-(currSum-ret[-1])
                ret[-2]+=ret[-1]
                ret.pop()
                return [num*2 for num in ret]
        return [finalSum*2]

class FenwickTree():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for i in range(N+1)]

    def construct(self,aa):
        for i in range(len(aa)):
            self.add(i,aa[i])

    def add(self, index, value):
        index += 1
        while index <= self.N:
            self.bit[index] += value
            index += (index & -index)

    def prefixSum(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans += self.bit[index]
            index -= (index & -index)
        return ans

    def print(self):
        print(self.bit)

    def query(self,start,end): # return the sum of [start,end)
        return self.prefixSum(end-1)-self.prefixSum(start-1)





class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        BITL=FenwickTree(len(nums1))
        BITR=FenwickTree(len(nums1))
        BITR.construct([1]*len(nums1))
        indexes={n:i for i,n in enumerate(nums1)}
        nums2=[indexes[n] for n in nums2]
        ans=0
        for num in nums2:
            left=BITL.query(0,num)
            right=BITR.query(num+1,len(nums1))
            ans+=left*right
            BITL.add(num,1)
            BITR.add(num,-1)
        return ans
