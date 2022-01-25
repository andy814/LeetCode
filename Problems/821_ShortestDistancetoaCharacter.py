from typing import *
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res=[]
        cIdx=[idx for idx,char in enumerate(s) if char==c]
        prev=next=cIdx[0]
        currCIdx=0
        for i in range(len(s)):
            res.append( min(abs(i-prev),abs(next-i))  ) 
            if i>=next:
                currCIdx+=1
                prev=next
                next=cIdx(currCIdx)
