import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m,n)