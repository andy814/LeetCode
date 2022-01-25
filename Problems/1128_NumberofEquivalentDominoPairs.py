import collections
from typing import *  
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoDict=collections.defaultdict(lambda:0)
        count=0
        for domino in dominoes:
            count+=dominoDict[(domino[0],domino[1])]
            if domino[0]!=domino[1]:
                count+=dominoDict[(domino[1],domino[0])]
            dominoDict[(domino[0],domino[1])]+=1          
        return count