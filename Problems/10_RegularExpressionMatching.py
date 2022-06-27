from typing import *
from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        a_idx=ord('a')
        alphabet=[ chr(a_idx+i) for i in range(26)]

        @cache
        def chMatch(sch,pch):
            if pch==".":
                return True
            if sch==pch:
                return True
            return False
            
        @cache
        def dp(s,p):
            if len(s)+len(p)==0:
                return True
            if len(s)==0:
                if p[-1] in alphabet or p[-1]==".":
                    return False
                for i,ch in enumerate(p[:-1]):
                    if (p[i] in alphabet or p[i]==".") and p[i+1] != "*":
                        return False
                return True
            if len(p)==0: # len(s)!=0
                return False
            
            if len(p)==1 or p[1]!="*": # single match
                return chMatch(s[0],p[0]) and dp(s[1:],p[1:])

            # multiple match
            if dp(s,p[2:]): # * for zero
                return True

            sidx=0 
            while sidx<len(s) and chMatch(s[sidx],p[0]):
                if dp(s[sidx+1:],p[2:]):
                    return True
                sidx+=1
            return False
        return dp(s,p)      