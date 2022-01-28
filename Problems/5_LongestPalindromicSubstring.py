class Solution:
    def longestPalindrome(self, s: str) -> str: # O(n^3)
        maxPal=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                subStr=s[i:j+1]
                if subStr==subStr[::-1] and len(subStr)>len(maxPal):
                    maxPal=subStr
        return maxPal

    def longestPalindrome2(self, s: str) -> str: # O(n^3)
        def calcPal(curr,s):
            front=curr
            rear=curr
            while front<len(s) and rear>=0 and s[rear]==s[front]:
                front+=1
                rear-=1
            ans1=s[rear+1:front]
            ans2=""
            if curr+1<len(s) and s[curr]==s[curr+1]:
                front=curr+1
                rear=curr
                while front<len(s) and rear>=0 and s[rear]==s[front]:
                    front+=1
                    rear-=1
                ans2=s[rear+1:front]
            return ans1 if len(ans1)>len(ans2) else ans2

        ans=""
        curr=0
        while curr<len(s):
            pal=calcPal(curr,s)
            if len(pal)>len(ans):
                ans=pal
            curr+=1
        return ans