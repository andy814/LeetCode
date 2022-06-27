from typing import *
from sortedcontainers import SortedList
from collections import Counter
from functools import cache
from collections import deque

class Solution1:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        s=list(s)
        cands=set()
        uppers=set()
        lowers=set()
        for ch in s:
            if ch.isupper():
                uppers.add(ch)
            else:
                lowers.add(ch)
        for lo in lowers:
            if chr(ord(lo)-32) in uppers:
                cands.add(chr(ord(lo)-32))
        if not cands:
            return ""
        else:
            return max(cands)

# greedy
class Solution2:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0
        if num%2==1 and k%2==0:
            return -1
        if k==0:
            return 1 if num%10==0 else -1
        
        curr=num%10
        if curr==0:
            curr=10
            
        while curr%k!=0 and curr<=num:
            curr+=10
        if curr>num:
            return -1
        else:
            return curr//k

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        tail=k%10
        cands=[i for i in range(tail,num+1,10)]
        dp=[float("inf")]*(num+1)
        dp[0]=0
        for i in range(1,num+1):
            for cand in cands:
                if i>=cand:
                    dp[i]=min(dp[i],1+dp[i-cand])
                    
        if dp[num]==float("inf"):
            return -1
        else:
            return dp[num]
        


# 贪婪算法：结果是0的个数+从右往左不溢出最长字符串的1的个数
# 证明： (1)首先证明贪婪算法找到的子序列g，是所有等长子序列里面数字最小的子序列。设g的长度为len(g)
# 我们将贪婪算法找到的子序列分为两段：A段是左侧的0，B段是右侧的不溢出最长子字符串。
# 假设存在对应数字更小的等长子序列s，要么它在A段将一个0换成了1，要么在B段舍弃最右侧的数然后往左多取了一个数，而这个数一定是1
# 无论是哪种情况，都不会使对应的数字再变小（详细证明略),也就是说s不存在
# 在（1）的基础上，既然贪婪算法取的B段是最长的，这说明B段再往左取一个数就会溢出了。
# 既然贪婪算法找的len(g)+1的子序列会溢出，说明任意len(g)+1的子序列都会溢出
# 因此len(g)即为最长子序列。
class Solution3_greedy: 
    def longestSubsequence(self, s: str, k: int) -> int: # DP,O(n^2)
        i=len(s)-1
        while i>=0 and int(s[i:],2)<=k:
            i-=1
        i=i+1
        return s.count("0")+s[i:].count("1")



# 动态规划：
# dp[i]是一个一维数组，记录每一个长度的最小数字
# 然后我们发现空间可以优化，因为dp[i]只来自于dp[i-1]，换句话说只要记录前一项的每一个长度的最小数字就结束了
class Solution3_dp: 
    def longestSubsequence(self, s: str, k: int) -> int: # DP,O(n^2)        
        dp=[0]
        for ch in s:
            nbr=int(ch)
            if k>=dp[-1]*2+nbr:
                dp.append(dp[-1]*2+nbr)
            for i in range(len(dp)-1,0,-1):
                dp[i]=min(dp[i],2*dp[i-1]+nbr)
            #print(ch,dp)
        return len(dp)-1


class Solution_dp_TLE: # sometimes TLE
    def longestSubsequence(self, s: str, k: int) -> int: # DP,O(n^2)
        # i:length dp[i]: minimum number of corresponding length (after visiting each ch)

        dp=[k+1]*(len(s)+1)
        dp[0]=0
        for ch in s:
            nbr=int(ch)
            for j in range(len(s),0,-1):
                temp=dp[j-1]*2+nbr
                if temp<=k:
                    dp[j]=min(dp[j],temp)
        #print(dp)
        for i in range(len(s),-1,-1):
            if dp[i]<=k:
                return i


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int: # top-down
        sizeDict=dict()
        for price in prices:
            sizeDict[(price[0],price[1])]=price[2]
        
        @cache
        def dp(m,n):
            ans=0
            if (m,n) in sizeDict:
                ans=sizeDict[(m,n)]
            for i in range(1,m//2+1):
                ans=max(ans,dp(i,n)+dp(m-i,n))
            for i in range(1,n//2+1):
                ans=max(ans,dp(m,i)+dp(m,n-i))
            return ans

        return dp(m,n)

    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int: # bottom-up
        dp=[[0]*n for _ in range(m)]
        sizeDict=dict()
        for price in prices:
            sizeDict[(price[0],price[1])]=price[2]
        for r in range(m):
            for c in range(n):
                ans=0
                if (r+1,c+1) in sizeDict:
                    ans=sizeDict[(r+1,c+1)]
                for i in range((r+1)//2):
                    ans=max(ans,dp[i][c]+dp[r-i-1][c])
                for j in range((c+1)//2):
                    ans=max(ans,dp[r][j]+dp[r][c-j-1])
                dp[r][c]=ans
        #        print(r,c,ans) #1,2,6
        #print(dp)
        return dp[m-1][n-1]