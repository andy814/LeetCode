import collections
from typing import *
class Solution1:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        visited={}
        curr=original
        for num in nums:
            visited[num]=True
        while curr in visited:
            curr*=2
        return curr

class Solution2:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [0] if nums[0]==1 else [1] 

        prefix=[]
        count=0
        for num in nums:
            if num==1:
                count+=1
            prefix.append(count)
        total=prefix[-1]
        scores=[total]
        for i in range(1,len(nums)+1):
            scoreL=i-prefix[i-1]
            scoreR=total-prefix[i-1]
            scores.append(scoreL+scoreR)
        
        maxScore=max(scores)
        ret=[i for i,num in enumerate(scores) if num==maxScore]

        return ret

class Solution3:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str: # O(s*klogk)
        def calcHash(sub,power,modulo):
            hash=0
            for i,char in enumerate(sub): 
                val = ord(char) - 96 # record
                hash+=val*power**i
            return hash%modulo
        for i in range(len(s)):
            sub=s[i:i+k]
            if calcHash(sub,power,modulo)==hashValue:
                return sub

    def subStrHash2(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str: # O(s+logk), TLE, 29/90
        preprocess=collections.defaultdict(lambda:[])
        for i in range(1+96,27+96):
            for p in range(k):
                if p==0:
                    preprocess[chr(i)].append( (i-96) )
                else:
                    preprocess[chr(i)].append( preprocess[chr(i)][-1]*power )
        hash=0
        sub=s[:k]
        for i,char in enumerate(sub):
            hash+=preprocess[char][i]
        if hash%modulo==hashValue:
            return sub
        for i in range(1,len(s)-k+1):
            hash-=preprocess[s[i-1]][0]
            hash//=power
            hash+=preprocess[s[i+k-1]][k-1]
            if hash%modulo==hashValue:
                return s[i:i+k]
        print("term")

    def subStrHash3(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str: #O(s+k)
        hash=0
        temp=1
        for i in range(len(s)-k+1):
            if i==0:
                for j in range(k):
                    hash+=(ord(s[j])-96)*temp
                    temp*=power

            else:
                hash-=ord(s[i-1])-96
                hash+=temp*(ord(s[i+k-1])-96)
                hash//=power

            if hash%modulo==hashValue:
                return s[i:i+k]

    def subStrHash4(self, s: str, power: int, mod: int, k: int, hashValue: int) -> str: # O(s+k), remove deletion by traversing in the reversed order, but still TLE sometimes
        
        orD={}
        for i in range(1,27):
            orD[chr(i+96)]=i
            
        hash=0
        temp=1
        
        ans=""
        for i in range(len(s)-k,-1,-1):
            if i==len(s)-k:
                for j in range(k):
                    hash+=(orD[s[i+j]])*temp
                    if j < k-1:
                        temp*=power
            else:
                hash-=(orD[s[i+k]])*(temp)
                hash*=power
                hash+=(orD[s[i]])
            if hash%mod==hashValue:
                ans=s[i:i+k]
        return ans

#Solution4
class Solution:
    class UnionFind():
        def __init__(self,n):
            self.p=list(range(n))
            self.rank=[1]*n
            self.size=[1]*n
        
        def find(self,i):
            if i!=self.p[i]:
                self.p[i]=self.find(self.p[i])
            return self.p[i]

        def union(self,i,j):
            rooti=self.find(i)
            rootj=self.find(j)

            if rooti==rootj:
                return

            if self.rank[rooti]>self.rank[rootj]:
                self.p[rootj]=rooti
                self.size[rooti]+=self.size[rootj]
                self.size[rootj]=0
            elif self.rank[rooti]<self.rank[rootj]:
                self.p[rooti]=rootj
                self.size[rootj]+=self.size[rooti]
                self.size[rooti]=0
            else:
                self.p[rootj]=rooti
                self.rank[rooti]+=1
                self.size[rooti]+=self.size[rootj]
                self.size[rootj]=0

    def groupStrings(self, words: List[str]) -> List[int]:

        def encode(word):
            ret=0
            for char in word:
                offset=ord(char)-ord("a")
                ret|=1<<offset
            return ret

        UF=Solution.UnionFind(len(words))
        visited={}
        for i,word in enumerate(words):
            mask=encode(word)
            if mask in visited:
                UF.union(visited[mask],i)
            visited[mask]=i
            for j in range(26):
                if mask&(1<<j)!=0:
                    if mask^(1<<j) in visited:
                        UF.union(visited[mask^(1<<j)],i)
                    visited[mask^(1<<j)]=i

        for i in range(len(words)):
            UF.find(i)

        return [ len(set(UF.p)),max(UF.size) ]

    

sol=Solution()
print(sol.groupStrings(["a","b","ab","cde"]))