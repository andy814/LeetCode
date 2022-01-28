import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret=0
        visiting=[]
        for char in s:
            visiting.append(char)
            charIdx=visiting.index(char)
            if charIdx!=len(visiting)-1:
                del visiting[:charIdx+1]
            ret=max(ret,len(visiting))
        return ret
    def lengthOfLongestSubstring2(self, s: str) -> int:
        charDict=collections.defaultdict(lambda:0)
        ret=0
        l=0
        for r in range(len(s)):
            curr=s[r]
            charDict[curr]+=1
            while charDict[curr]>1:
                charDict[s[l]]-=1
                l+=1
            ret=max(ret,r-l+1)
        return ret
        
            