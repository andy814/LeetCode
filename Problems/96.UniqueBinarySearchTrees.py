from functools import cache
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def recur(start,end):
            if start==end:
                return 1
            ret=0
            for i in range(start,end):
                ret+=recur(start,i)*recur(i+1,end)
            return ret
        return recur(0,n)
