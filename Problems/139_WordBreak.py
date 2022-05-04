from pickle import TRUE
from re import T
from typing import *
from collections import deque
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: # O(n^3)
        wordSet=set()
        for word in wordDict:
            wordSet.add(word)

        @cache
        def recur(s):
            if len(s)==1:
                return s in wordSet
            if s in wordSet:
                return True
            for i in range(len(s)-1):
                if recur(s[:i+1]) and recur(s[i+1:]):
                    return True
            return False

        return recur(s)


        
