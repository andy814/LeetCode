from typing import *
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ret=0
        #g.sort()
        for cookie in s:
            ret+=self.findMin(g,cookie)
        return ret

    def findMin(self,g,cookie):
        if not g:
            return 0
        minG=0
        flag=False
        for greed in g:
            if cookie-greed>=0 and cookie-greed<cookie-minG:
                minG=greed 
                flag=True
        if flag:
            g.remove(minG)
            return 1
        else:
            return 0

    def findContentChildren2(self, g: List[int], s: List[int]) -> int: # slogs+glogg
        g.sort()
        s.sort()
        count=gIdx=sIdx=0
        while gIdx<len(g) and sIdx<len(s):
            if s[sIdx]>=g[gIdx]:
                gIdx+=1
                count+=1
            sIdx+=1
        return count