from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #@lru_cache(None)
        def recur(x,n):
            if n==1:
                return x
            else:
                half=recur(x,n>>1)
                if n&1:
                    return x*half*half
                else:
                    return half*half
        if n>0:
            return recur(x,n)
        elif n==0:
            return 1
        else:
            return 1/recur(x,-n)
        
class Solution2: # source: https://github.com/azl397985856/leetcode/blob/master/problems/50.pow-x-n.md
    def myPow(self, x: float, n: int) -> float: # no recur
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        while n:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res