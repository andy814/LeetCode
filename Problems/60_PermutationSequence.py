from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nList="".join([str(i) for i in range(1,n+1)])
        perm=list(permutations(nList))
        perm.sort()
        return "".join( perm[k-1] )
