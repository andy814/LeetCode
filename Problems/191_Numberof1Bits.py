class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=bin(n)
        return len([i for i in binary if i=="1"])