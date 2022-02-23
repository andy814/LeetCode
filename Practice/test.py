# source: https://leetcode.com/problems/count-good-triplets-in-an-array/discuss/1783185/Python-O(NlogN)-2-Solutions-using-Fenwick-Tree
from sys import prefix


class FenwickTree():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for i in range(N+1)]

    def add(self, index, value):
        index += 1
        while index <= self.N:
            self.bit[index] += value
            index += (index & -index)

    def prefixSum(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans += self.bit[index]
            index -= (index & -index)
        return ans

    def print(self):
        for i in self.bit:
            print(i,end=" ")
        print()

    def query(self,start,end): # return the sum of [start,end)
        return self.prefixSum(end-1)-self.prefixSum(start-1)

aa=FenwickTree(5)

for i in range(5):
    aa.add(i,2)
aa.add(0,12)
print(aa.prefixSum(-1))
print(aa.query(0,3))