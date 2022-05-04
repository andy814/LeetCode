from shutil import move
from typing import *
from collections import defaultdict
from collections import deque
from functools import cache
class Solution1:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        ans=[]
        ans.append(list(nums1-nums2))
        ans.append(list(nums2-nums1))
        return ans

class Solution2:
    def minDeletion(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        curr=1
        beautiful=[nums[0]]
        ret=0
        needMatch=True
        while curr<len(nums):
            #print(beautiful,nums[curr],needMatch)
            if needMatch:
                if nums[curr]==beautiful[-1]:
                    #print("adding")
                    ret+=1
                else:
                    beautiful.append(nums[curr])
                    needMatch=False
            else:
                beautiful.append(nums[curr])
                needMatch=True    
            curr+=1
        
        if len(beautiful)&1:
            #print("adding")
            ret+=1
        return ret


class Solution3:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res=[]
        def calcQuery(query):
            ans=0
            maxLimit=9* (10** ( (intLength-1)//2 ) )
            if query>maxLimit:
                ans=-1
            else:
                query-=1
                halfNbr=(intLength+1)//2 
                isEven=not intLength&1
                halfNbrList=[0]*halfNbr
                halfNbrList[0]=1
                while query>0:
                    halfNbr-=1
                    lastDigit=query%10
                    query//=10
                    halfNbrList[halfNbr]+=lastDigit
                halfNbrList=list(halfNbrList)
                if len(halfNbrList)>1 and not isEven:
                    repeat=halfNbrList[:-1]
                    halfNbrList.extend(repeat[::-1])
                elif len(halfNbrList)>1 and isEven:
                    repeat=halfNbrList
                    halfNbrList.extend(repeat[::-1])
                elif len(halfNbrList)==1 and isEven:
                    halfNbrList.append(halfNbrList[0])
                ans= int("".join( str(nbr) for nbr in halfNbrList ) )
            res.append(ans)
 
        for query in queries:
            calcQuery(query)
        return res

class Solution4:

    '''
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int: # TLE
        pileCount=defaultdict(list)
        for i in range(len(piles)):
            sum=0
            for j in range( min(len(piles[i]),k+1) ):
                sum+=piles[i][j]
                pileCount[i].append(sum)
                
        @cache
        def dp(start,movesLeft):
            if movesLeft==0:
                return 0
            if start>=len(piles):
                return 0
            ans=-1
            for i in range(movesLeft+1): # the algo fails here ( worst time: len(piles)*k*k )
                if i==0:
                    ans=max(ans,dp(start+1,movesLeft))
                elif len(piles[start])<i: 
                    ans=max(ans, dp(start+1,movesLeft-len(piles[start])) + pileCount[start][-1])
                else:
                    ans=max(ans, dp(start+1,movesLeft-i)+pileCount[start][i-1]  )
            return ans

        return dp(0,k)
    '''

class Solution4:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int: # works
                
        @cache
        def dp(start,movesLeft):
            if movesLeft==0:
                return 0
            if start==len(piles):
                return 0
            ans=dp(start+1,movesLeft)
            pileCount=0
            for i in range(1,min(len(piles[start])+1,movesLeft+1)):
                pileCount+=piles[start][i-1]
                ans=max(ans, dp(start+1,movesLeft-i)+pileCount  )
            return ans

        return dp(0,k)


    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int: # theoretically faster, but actually same speed
        pileCount=defaultdict(list)
        for i in range(len(piles)):
            sum=0
            for j in range( min(len(piles[i]),k+1) ):
                sum+=piles[i][j]
                pileCount[i].append(sum)
                
        @cache
        def dp(start,movesLeft): # total time complexity: O(M^2, M=sum(piles[i].length))
            if movesLeft==0:
                return 0
            if start>=len(piles):
                return 0
            ans=dp(start+1,movesLeft)
            for i in range(1,min(len(piles[start])+1,movesLeft+1)):
                ans=max(ans, dp(start+1,movesLeft-i)+pileCount[start][i-1]  )
            return ans

        return dp(0,k)