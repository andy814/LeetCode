import collections
from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: # TLE
        ret=[]
        def dfs(targetLeft,currSol,candidates,start):
            for i in range(start,len(candidates)):
                diff=targetLeft-candidates[i]
                ans=currSol.copy()
                ans.append(candidates[i])
                if diff<0:
                    return
                elif diff==0:
                    ret.append(ans)
                else: # diff>0:
                    dfs(diff,ans,candidates,i+1)
        candidates.sort()
        dfs(target,[],candidates,0)
        retUniq=set( [ tuple(sorted(lst)) for lst in ret ] )
        return retUniq

class Solution:
    def combinationSum2_improved(self, candidates: List[int], target: int) -> List[List[int]]: 
        # we merge the candidates with the same values using dict to prevent the searching tree from growing too high
        eleCount=collections.defaultdict(int)
        for cand in candidates:
            eleCount[cand]+=1

        candSet=list(set(candidates))
        candSet.sort() # sorted set
        ret=[]
        
        def dfs(targetLeft,currSol,candSet,start): # maximum height: len(candSet)
            for i in range(start,len(candSet)):
                for j in range(1,eleCount[candSet[i]]+1):
                    diff=targetLeft-candSet[i]*j
                    ans=currSol.copy()
                    ans+=[candSet[i]]*j
                    if diff<0:
                        break
                    elif diff==0:
                        ret.append(ans)
                    else: # diff>0:
                        dfs(diff,ans,candSet,i+1)
        
        candidates.sort()
        dfs(target,[],candSet,0)
        return ret