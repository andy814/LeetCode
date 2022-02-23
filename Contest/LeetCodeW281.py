from math import gcd
from typing import *
import collections

class Solution1:
    def countEven(self, num: int) -> int:
        def digitSum(num):
            strNum=str(num)
            ret=0
            for digit in strNum:
                ret+=int(digit)
            return ret
        ret=0
        for i in range(1,num+1):
            if not digitSum(i)&1:
                ret+=1
        return ret

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2: # 再做一遍，用链表
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        sumNbr=0
        modifiedVals=[]
        for num in vals[1:]:
            if num==0:
                if sumNbr!=0:
                    modifiedVals.append(sumNbr)
                    sumNbr=0
            else:
                sumNbr+=num
        sentinel=ListNode()
        curr=sentinel
        for num in modifiedVals:
            next=ListNode(num)
            curr.next=next
            curr=next
        return sentinel.next

class Solution3:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        charCount=collections.defaultdict(int)
        for char in s:
            charCount[char]+=1
        charList=list(sorted([list(tup) for tup in charCount.items()],reverse=True))
        ret=""

        def recur(listIdx):
            if listIdx>=len(charList):
                return
            nonlocal ret
            numLeft=charList[listIdx][1]
            char=charList[listIdx][0]
            processingIdx=listIdx+1
            while numLeft and processingIdx<len(charList):
                toAppend=min(numLeft,repeatLimit)
                ret+=char*toAppend
                numLeft-=toAppend
                if numLeft:
                    ret+=charList[processingIdx][0]
                    charList[processingIdx][1]-=1
                    if charList[processingIdx][1]==0:
                        processingIdx+=1
            if numLeft:
                toAppend=min(numLeft,repeatLimit)
                ret+=char*toAppend
            recur(processingIdx)

        recur(0)
        return ret            

class Solution4:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        gcdCounter=collections.Counter()
        for num in nums:
            num_gcd=gcd(num,k)
            for g in gcdCounter:
                if g*num_gcd%k==0:
                    count+=gcdCounter[g]
            gcdCounter[num_gcd]+=1
        return count


