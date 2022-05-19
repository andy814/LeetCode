import functools
class Solution:
    def numSquares(self, n: int) -> int: # TLE
        cands= [i**2 for i in range(1,101)]
        @functools.cache
        def dp(i,target):
            if target<0:
                return float("inf")
            elif target==0:
                return 0
            if i>len(cands):
                return float("inf")
            if cands[i]>target:
                return float("inf")

            ans=float("inf")
            
            if cands[i]==1:
                for j in range(4):
                    #print(j)
                    cand=j+dp(i+1,target-cands[i]*j)
                    ans=min(cand,ans)
                return ans
            else:
                for j in range(min(cands[i],(target//cands[i]+1))):
                    cand=j+dp(i+1,target-cands[i]*j)
                    ans=min(cand,ans)
                return ans
            
        ret= dp(0,n)
        return ret

    def numSquares(self, n: int) -> int:
        cands= [i**2 for i in range(1,101) if i**2<=n]
        dp=[float("inf")]*(n+1)
        for cand in cands:
            if cand<=n:
                dp[cand]=1
        for i in range(1,n+1):
            for cand in cands:
                if i-cand>=0:
                    dp[i]=min(dp[i],dp[i-cand]+1)
        return dp[n]
        