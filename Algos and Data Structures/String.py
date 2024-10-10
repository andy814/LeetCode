
from typing import *

# source: https://oi-wiki.org/string/z-func/
# computer_lcp(largest common prefix)
# return: 函数z[i],为s和s[i,n-1]（即以i开头的后缀）的最长公共前缀的长度
# 返回一个字串的每个后缀之中，与字串开头相同的最长前缀。
# time complexity: O(n)
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

# source: https://towardsdatascience.com/pattern-search-with-the-knuth-morris-pratt-kmp-algorithm-8562407dba5b
# Longest Proper Prefix which is Suffix (LPS) array
# return: 子串s[0,...,i]中最长的相等的真前缀与真后缀的长度。
# <或> 返回一个字串的每个前缀之中，与字串开头相同的次长后缀。
# 和z函数相比，两个方法里面返回列表的第一项都是0
def compute_lps(pattern: str) -> List[int]:
    # Longest Proper Prefix that is suffix array
    lps = [0] * len(pattern)

    prefi = 0
    for i in range(1, len(pattern)):
        
        # Phase 3: roll the prefix pointer back until match or 
        # beginning of pattern is reached
        while prefi and pattern[i] != pattern[prefi]:
            prefi = lps[prefi - 1]

        # Phase 2: if match, record the LSP for the current `i`
        # and move prefix pointer
        if pattern[prefi] == pattern[i]:
            prefi += 1
            lps[i] = prefi

        # Phase 1: is implicit here because of the for loop and 
        # conditions considered above

    return lps

# find a substring of length m from a string of length n in O(m+n)
# Knuth-Morris-Pratt Algorithm
# time: O(m+n), space: O(m), m=len(text),n=len(pattern)
def kmp(pattern: str, text: str) -> List[int]:
    match_indices = []
    pattern_lps = compute_lps(pattern)

    patterni = 0
    for i, ch in enumerate(text):
        
        # Phase 3: if a mismatch was found, roll back the pattern
        # index using the information in LPS
        while patterni and pattern[patterni] != ch:
            patterni = pattern_lps[patterni - 1]

        # Phase 2: if match
        if pattern[patterni] == ch:
            # If the end of a pattern is reached, record a result
            # and use infromation in LSP array to shift the index
            if patterni == len(pattern) - 1:
                match_indices.append(i - patterni)
                patterni = pattern_lps[patterni]
            
            else:
                # Move the pattern index forward
                patterni += 1

        # Phase 1: is implicit here because of the for loop and 
        # conditions considered above

    return match_indices

print(kmp("dya","andyandyandy"))