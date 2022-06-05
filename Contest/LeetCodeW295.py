from typing import *
from collections import Counter
from functools import cache
from collections import deque
from cv2 import split

class Solution1:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        targetCtr=Counter(target)
        sCtr=Counter(s)
        ans=0
        while sCtr.most_common()[-1][1]>=0:
            ans+=1
            sCtr.subtract(targetCtr)
        return ans-1

class Solution2:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def isMoney(word): # O(n)
            if not word:
                return False
            prefix=word[0]
            nbr=word[1:]
            if prefix!="$":
                return False
            splitted=nbr.split(".")
            if len(splitted)==1:
                return nbr.isdecimal()
            elif len(splitted)==2:
                return splitted[0].isdecimal() and splitted[1].isdecimal()
            else:
                return False

        rephrase=[]
        for word in sentence.split(" "): # O(sentence*word)
            if isMoney(word):
                discounted="%.2f" % round(float(word[1:])*(100-discount)*0.01,2)
                rephrase.append("$"+str(discounted))
            else:
                rephrase.append(word)
        
        return " ".join(word for word in rephrase)

class Solution3: #  关键点：dp[i]表示第i个元素向右删除，直到删到不能再删的状态，这期间经过的最短时间。
    #每次从单调栈里面拿元素都相当于动态规划，假设目前处理的是A[i]，拿出来的元素是b，dp[i]就会更新从A[i]到b右侧的第一个更大元素的最小删除轮数。
    #更新原则：max(dp[i]+1,steps), 也就是说看看是从A[i]删到b左侧再+1费时（恰好由上一步dp求出），还是从b删到下一个更大元素（也就是b不能再删时）费时（之前已求出），总时间取max
    #这样会从栈里面一直拿，直到栈里的元素都大于A[i]，这个时候dp[i]最后一次更新就是表示第i个元素向右删除，直到删到不能再删的状态，这期间经过的最短时间。
    def totalSteps(self, A: List[int]) -> int:
        n=len(A)
        dp=[0]*len(A)
        mono=[]
        for i in range(n-1,-1,-1):
            while mono and A[i]>mono[-1][0]:
                top,steps=mono.pop()
                dp[i]=max(dp[i]+1,steps)
            mono.append((A[i],dp[i]))
        return max(dp)


class Solution4:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        heap = [(0,0,0)]
        dist = [[float("inf")]*n for _ in range(m)]
        dist[0][0]=0
        visited=set()
        while heap and len(visited)<m*n:
            time,r,c = heapq.heappop(heap)
            if (r,c) not in visited:
                cands=[(r-1,c),(r,c+1),(r+1,c),(r,c-1)]
                visited.add((r,c))
                for nr,nc in cands:
                    if 0<=nr<m and 0<=nc<n:
                        obs=grid[nr][nc]
                        if (nr,nc) not in visited and dist[nr][nc]>time+obs:
                            dist[nr][nc]=time+obs
                            heapq.heappush(heap, (time+obs,nr,nc))

        return dist[m-1][n-1]            


class Solution4: # without visited, faster
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        heap = [(0,0,0)]
        dist = [[float("inf")]*n for _ in range(m)]
        dist[0][0]=0
        while heap:
            time,r,c = heapq.heappop(heap)
            cands=[(r-1,c),(r,c+1),(r+1,c),(r,c-1)]
            for nr,nc in cands:
                if 0<=nr<m and 0<=nc<n:
                    obs=grid[nr][nc]
                    if dist[nr][nc]>time+obs:
                        dist[nr][nc]=time+obs
                        heapq.heappush(heap, (time+obs,nr,nc))

        return dist[m-1][n-1]            