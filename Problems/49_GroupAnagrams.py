from collections import Counter,defaultdict
from typing import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        CounterDict=defaultdict(list)
        for str in strs: 
            #CounterDict[frozenset(Counter(str).items())].append(str) # 250ms
            CounterDict[tuple(sorted(str))].append(str) # 100ms
        return CounterDict.values()