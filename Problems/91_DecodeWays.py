from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str,start=0) -> int:
        
        if int(s[start])==0:
            return 0

        if start==len(s)-1:
            return 1

        if 3<=int(s[start])<=9:
            return self.numDecodings(s,start+1)
        
        if int(s[start])==1 or ( int(s[start])==2 and  int(s[start+1])<=6 ):
            if start==len(s)-2:
                return 1+self.numDecodings(s,start+1)
            else:
                return self.numDecodings(s,start+1)+self.numDecodings(s,start+2)
        
        else:
            return self.numDecodings(s,start+1)
        