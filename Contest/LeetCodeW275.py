import collections
from typing import *
class Solution1:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        
        for i in range(n):
            visited=set({})
            for j in range(n):
                if matrix[i][j] in visited:
                    return False
                visited.add(matrix[i][j])
        
        for j in range(n):
            visited=set({})
            for i in range(n):
                if matrix[i][j] in visited:
                    return False
                visited.add(matrix[i][j])
        return True
                
class Solution2: # 看答案怎么写的
    def minSwaps(self, nums: List[int]) -> int:
        count1=0
        for num in nums:
            if num==1:
                count1+=1
        if count1==0 or count1==len(nums):
            return 0 
        max1=self.maxWindow1(nums,count1) # end not included
        return count1-max1

    def maxWindow1(self,nums,wsize):
        start=0
        end=wsize # end not included
        count1=0
        for i in range(start,end):
            if nums[i]==1:
                count1+=1
        ret=count1
        #print("wsize:",wsize)
        while start<len(nums):
            #print("count1:",count1)
            change=0
            if nums[start]==1:
                change-=1
            if nums[end]==1:
                change+=1
            start+=1
            end+=1
            if end==len(nums):
                end=0
            count1+=change
            ret=max(ret,count1)

        return ret

'''
class Solution3: # O(n^2)
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        wordLength=collections.defaultdict(list)
        for word in startWords:
            wordLength[len(word)].append(word)
        #print(wordLength)
        count=0
        cache=startWords[0]
        for target in targetWords:
            if len(set(cache)-set(target))==0:
                count+=1
                continue
            for start in wordLength[len(target)-1]:
                if len(set(start)-set(target))==0:
                    count+=1
                    cache=start
                    break
        return count
'''

class Solution3: # O(n)
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        wordLength=collections.defaultdict(set)
        for word in startWords:
            wordLength[len(word)].add(frozenset(word))
        count=0
        for target in targetWords:
            for char in target:
                #targetSet=set(target)
                #targetSet.remove(char)
                tryTarget=target.replace(char,"")
                tryTargetSet=frozenset(tryTarget)
                if tryTargetSet in wordLength[len(target)-1]:
                    count+=1
                    break
        return count

class Solution4:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        totalTime,currTime=0,0
        sortedTime=sorted(zip(growTime,plantTime),reverse=True) # sort by growtime
        #print(sortedTime)
        for gt,pt in sortedTime:
            currTime+=pt
            totalTime=max(totalTime,currTime+gt)
            #print(currTime,totalTime)
        return totalTime

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        currTime, bloomTime = 0, []
        # sort seeds by growTime in descending order
        # All you need to do is to plant the longest growing seeds first
        for [g, p] in sorted([[growTime[i], plantTime[i]] for i in range(len(plantTime))], reverse=True):
            bloomTime.append(currTime + g + p)
            currTime += p
            print(bloomTime)
        return max(bloomTime)

sol=Solution4().earliestFullBloom([1,4,3],[2,3,1])
