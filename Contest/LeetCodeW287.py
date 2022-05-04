from email.policy import default
from shutil import move
from typing import *
from collections import defaultdict
from collections import deque
from functools import cache
from collections import Counter

class Solution1:
    def convertTime(self, current: str, correct: str) -> int:
        currH=int(current[:2])
        currM=int(current[3:])
        targetH=int(correct[:2])
        targetM=int(correct[3:])

        ops=0
        if currM<=targetM:
            ops=targetH-currH
            minLeft=targetM-currM
        else:
            ops=targetH-currH-1
            minLeft=targetM-currM+60

        while minLeft>=15:
            minLeft-=15
            ops+=1
        while minLeft>=5:
            minLeft-=5
            ops+=1
        while minLeft>=1:
            minLeft-=1
            ops+=1
        return ops


class Solution2:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        noLose=set()
        oneLose=set()
        for match in matches:
            noLose.add(match[0])
            noLose.add(match[1])
        for match in matches:
            loser=match[1]
            if loser in noLose:
                noLose.remove(loser)
                oneLose.add(loser)
            elif loser in oneLose:
                oneLose.remove(loser)
            
        return [sorted(list(noLose)),sorted(list(oneLose))]


class Solution3:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sumCand=sum(candies)
        if k>sumCand:
            return 0

        candies.sort()
        start=0
        end=k//sumCand
        ans=0
        while start<=end:
            mid=(start+end)//2
            allocate=0
            for num in candies:
                allocate+=num//mid
            if allocate>=k:
                ans=max(0,mid)
                start=mid+1
            else:
                end=mid-1
        return ans

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
class Encrypter: # TLE

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        #self.keys=keys
        #self.values=values
        self.dictionary=set(dictionary)
        self.mapping=defaultdict()
        for i,key in enumerate(keys):
            self.mapping[key]=values[i]
        self.revMapping=defaultdict(set)
        for i,value in enumerate(values):
            self.revMapping[value].add(keys[i])
        self.possibleDict=defaultdict(set)
        for string in self.dictionary:
            for i,ch in enumerate(string):
                self.possibleDict[i].add(ch)

    def encrypt(self, word1: str) -> str:
        ret=""
        for ch in word1:
            ret+=self.mapping[ch]
        return ret

    def decrypt(self, word2: str) -> int:
        ans=[]
        for i in range(0,len(word2),2):
            keySet=self.revMapping[word2[i:i+2]]
            keySet=keySet&self.possibleDict[i//2]
            
            if i==0:
                for key in keySet:
                    ans.append([key])
                continue
                
            nextAns=[]
            for ansList in ans:
                for key in keySet:
                    ansList.append(key)
                    nextAns.append(ansList.copy())
                    ansList.pop()
            ans=nextAns
            
        tupAns=set( [tuple(li) for li in ans]  )
        ans=set()
        for tup in tupAns:
            ans.add("".join(ch for ch in tup))
        
        return len(ans&self.dictionary)            
            
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]): #accepted
        self.dictionary=set(dictionary)
        self.mapping=defaultdict()
        for i,key in enumerate(keys):
            self.mapping[key]=values[i]
        self.revMapping=defaultdict(set)
        for i,value in enumerate(values):
            self.revMapping[value].add(keys[i])

    def encrypt(self, word1: str) -> str:
        ret=""
        for ch in word1:
            ret+=self.mapping[ch]
        return ret

    def decrypt(self, word2: str) -> int: # 200
        tempDict=self.dictionary.copy()
        for diction in tempDict.copy():
            if len(diction)!=len(word2)//2:
                tempDict.remove(diction)
        
        for i in range(0,len(word2),2): # 100
            keySet=self.revMapping[word2[i:i+2]]
            for diction in tempDict.copy(): # 100
                if diction[i//2] not in keySet:
                    tempDict.remove(diction)
        return len(tempDict)            
            

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):

        self.mapping=defaultdict()
        for i,key in enumerate(keys):
            self.mapping[key]=values[i]
        self.possibleEncrypts=Counter()
        for diction in dictionary:
            self.possibleEncrypts[self.encrypt(diction)]+=1
            
    def encrypt(self, word1: str) -> str:
        ret=""
        for ch in word1:
            ret+=self.mapping[ch]
        return ret

    def decrypt(self, word2: str) -> int: # 200
        return self.possibleEncrypts[word2] 
            


            