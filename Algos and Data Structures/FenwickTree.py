# source: https://leetcode.com/problems/count-good-triplets-in-an-array/discuss/1783185/Python-O(NlogN)-2-Solutions-using-Fenwick-Tree
class FenwickTree():
    def __init__(self, N=0):
        self.N = N
        self.bit = [0 for i in range(N+1)]

    def construct(self,aa):
        self.N=len(aa)
        self.bit=[0 for i in range(self.N+1)]
        for i,num in enumerate(aa):
            self.add(i,num)


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
        print(self.bit)

    def query(self,start,end): # return the sum of [start,end)
        return self.prefixSum(end-1)-self.prefixSum(start-1)



# detailed explanation↓
# Source: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
# Python implementation of Binary Indexed Tree

# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BITTree,i):
	s = 0 #initialize result

	# index in BITree[] is 1 more than the index in arr[]
	i = i+1

	# Traverse ancestors of BITree[index]
	while i > 0:

		# Add current element of BITree to sum
		s += BITTree[i]

		# Move index to parent node in getSum View
		i -= i & (-i)
	return s

# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree , n , i ,v):

	# index in BITree[] is 1 more than the index in arr[]
	i += 1

	# Traverse all ancestors and add 'val'
	while i <= n:

		# Add 'val' to current node of BI Tree
		BITTree[i] += v

		# Update index to that of parent in update View
		i += i & (-i)


# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):

	# Create and initialize BITree[] as 0
	BITTree = [0]*(n+1)

	# Store the actual values in BITree[] using update()
	for i in range(n):
		updatebit(BITTree, n, i, arr[i])
	return BITTree


# Driver code to test above methods
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITTree = construct(freq,len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5)))
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6)
print("Sum of elements in arr[0..5]"+
					" after update is " + str(getsum(BITTree,5)))

# This code is contributed by Raju Varshney

# sum和update都是从下往上走，其中左孩子到父节点是i += i & (-i)，右孩子到父节点是i -= i & (-i)
# 也可以理解为i += i & (-i)是向上走，直到通过右拐遇到祖先节点。i -= i & (-i)向上走，直到通过左拐遇到祖先节点（未证明）
# 并不总是树形，比如n=5时会有一个节点是分离态（因为6没加进去）。但是不妨碍算法运行。
# 这个数据结构没用数组的第0项。
# Fenwick Tree的元素个数是固定的，不过可以提前弄一堆为0的元素来模拟变化（和使用数组同样道理），置0为去除，0置其他数为添加

FT=FenwickTree(5)
FT.add(0,1)
print(FT.bit)
print(FT.query(1,4))
