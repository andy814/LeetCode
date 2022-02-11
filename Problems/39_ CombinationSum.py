from typing import *    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        visited=[] # list[list]
        result=set({})
        def dfs(currSol,targetLeft):
            nonlocal visited
            nonlocal result
            for cand in candidates:
                if cand==targetLeft:
                    currSol.append(cand)
                if 
                visited.append(currSol.copy())


        dfs([],target)
        return list(result)
        '''

        result=[]
        def dfs(currSol,targetLeft):
            nonlocal result
            for cand in candidates:
                if cand==targetLeft:
                    ans=currSol.copy()
                    ans.append(cand)
                    result.append(ans)
                elif cand<targetLeft:
                    ans=currSol.copy()
                    ans.append(cand)
                    dfs(ans,targetLeft-cand)
        dfs([],target)
        resultUniq=set([tuple(sorted(sol)) for sol in result])
        return list(resultUniq)
