from functools import cache
class Solution1: # TLE
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


class Solution2: # TLE
    def longestPalindrome(self, s: str) -> str: # O(n^3)
        @cache
        def dp(start,end):
            #print("start,end",start,end)
            if end-start==0:
                return s[start]
            elif end-start==1: 
                if s[end]==s[start]:
                    return s[start:end+1]
                else:
                    return s[start]
            else:
                if s[start+1:end]==dp(start+1,end-1) and s[start]==s[end]: 
                    return s[start:end+1]
                else:
                    left=dp(start+1,end)
                    right=dp(start,end-1)
                    return left if len(left)>len(right) else right
        return dp(0,len(s)-1)


class Solution3: # MLE
    def longestPalindrome(self, s: str) -> str:
        ans=[0,0]
        @cache
        def dp(start,end):
            #print("start,end",start,end)
            if end-start==0:
                return True
            elif end-start==1: 
                if s[end]==s[start]:
                    return True
                else:
                    return False
            else:
                return dp(start+1,end-1) and s[start]==s[end]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if j-i>ans[1]-ans[0] and dp(i,j):
                    ans=[i,j]
        return s[ans[0]:ans[1]+1]


class Solution4: # AC
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = [0,0]
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if i == j:
                    dp[i][j] = True
                elif j == i+1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and j - i > res[1]-res[0]:
                    res = [i,j]
                    #print("res:",res)
        #print(dp)
        return s[res[0]:res[1]+1]