from itertools import permutations
from typing import *
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set([tuple(seq) for seq in permutations(nums)]))