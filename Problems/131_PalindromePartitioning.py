from typing import *
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def dfs(start,part):
            if start>=len(s):
                return
            left=s[start:]
            if left==left[::-1]:
                result.append(part.copy())
            for i in range(start+1,len(s)):
                if s[start:i]==rev(s[start:i]):
                    part.append(i)
                    dfs(i,part)
                    part.pop()

        def getPartition(part):
            if len(part)==0:
                return [s]
            curr=0
            ret=[]
            while curr<len(part):
                if curr==0:
                    ret.append(s[:part[curr]])
                else:
                    ret.append(s[part[curr-1]:part[curr]])
                curr+=1
            ret.append( s[part[curr-1]:] ) 
            return ret
        
        def rev(s):
            return s[::-1]

        dfs(0,[])
        ans=[]
        for p in result:
            ans.append(getPartition(p))
        return ans