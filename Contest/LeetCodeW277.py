import collections
from tkinter.messagebox import RETRYCANCEL
from typing import *
class Solution1:
    def countElements(self, nums: List[int]) -> int:
        maxNum=max(nums)
        minNum=min(nums)
        res=len(nums)-nums.count(maxNum)-nums.count(minNum)
        return max(0,res)

class Solution2:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNums=[i for i in nums if i>0]
        negativeNums=[i for i in nums if i<0]
        ret=[]
        for i in range(len(positiveNums)):
            ret.append(positiveNums[i])
            ret.append(negativeNums[i])
        return ret

class Solution3:
    def findLonely(self, nums: List[int]) -> List[int]: # time limit exceeded because of remove
        nums.sort()
        ret=nums[:]
        for i in range(1,len(nums)-1):
            if nums[i+1]-nums[i]<=1 or nums[i]-nums[i-1]<=1:
                ret.remove(nums[i])
        if len(nums)>=2:
            if nums[1]-nums[0]<=1:
                if nums[0] in ret:
                    ret.remove(nums[0])
            if nums[-1]-nums[-2]<=1:
                if nums[-1] in ret:
                    ret.remove(nums[-1])
        return ret

    def findLonely2(self, nums: List[int]) -> List[int]: # nlogn
        nums.sort()
        ret=[]
        for i in range(1,len(nums)-1):
            if nums[i+1]-nums[i]>1 or nums[i]-nums[i-1]>1:
                ret.append(nums[i])
        if len(nums)>=2:
            if nums[1]-nums[0]>1:
                if nums[0] not in ret:
                    ret.append(nums[0])
            if nums[-1]-nums[-2]>1:
                if nums[-1] not in ret:
                    ret.append(nums[-1])
        return ret

    def findLonely3(self, nums: List[int]) -> List[int]: # O(n)
        check = collections.defaultdict(int)
        for i in nums:
            check[i] += 1
        ans = []
        for i in nums:
            if check[i]==1 and check[i+1]==0 and check[i-1]==0:
                ans.append(i)
        return ans

class Solution4: # bit-masking
    def maximumGood(self, statements: List[List[int]]) -> int:
        ret=0
        for i in range(2**len(statements)):
            personality=bin(i)[2:] # a string consisting of 0/1
            personality=personality.rjust(len(statements),"0") # left fill 0
            if self.isValid(personality,statements):
                ret=max(ret,personality.count("1"))
        return ret

    def isValid(self,personality,statements): # 0 for bad, 1 for good
        goodIdx=[]
        for i,num in enumerate(personality):
            if num=="1":
                goodIdx.append(i)
        for idx in goodIdx:
            judges=statements[idx]
            for j,judge in enumerate(judges):
                if judge!=2 and personality[j]!=judge:
                    return False
        return True

class Solution4_DFS: #backtrack 
    def maximumGood(self, statements: List[List[int]]) -> int:
        
        def DFS(personality):
            nonlocal statements
            nonlocal ret
            #personalityRecord=personality[:]
            if isValid(personality[:]):
                if len(personality)==len(statements):
                    ret=max(ret,personality.count(1))
            else:
                return
            if len(personality)<len(statements):
                personality.append(1)
                DFS(personality)
                personality[-1]=0
                DFS(personality)
                personality.pop()

        def isValid(personality):
            nonlocal statements
            lenRecord=len(personality)
            while len(personality)<len(statements):
                personality.append(0)
            for i in range(len(statements)):
                if personality[i]==1:
                    for j in range(lenRecord):
                        if statements[i][j]!=2 and statements[i][j]!=personality[j]:
                            return False
            return True

        ret=0        
        DFS([])
        return ret
