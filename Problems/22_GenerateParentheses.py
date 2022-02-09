from itertools import product
from typing import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret=[]
        def dfs(sol,numLeft,numRight,n):
            nonlocal ret
            if len(sol)==n*2:
                ret.append(sol)
            if numLeft<n:
                dfs(sol+"(",numLeft+1,numRight,n)
            if numRight<n and numRight<numLeft:
                dfs(sol+")",numLeft,numRight+1,n)
        return ret