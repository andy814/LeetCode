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



# detailed explanationâ†“
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

# sumĺ’Śupdateé?˝ć?Żä»Žä¸‹ĺľ€ä¸Ščµ°ďĽŚĺ…¶ä¸­ĺ·¦ĺ­©ĺ­?ĺ?°ç?¶čŠ‚ç‚ąć?Żi += i & (-i)ďĽŚĺŹłĺ­©ĺ­?ĺ?°ç?¶čŠ‚ç‚ąć?Żi -= i & (-i)
# äąźĺŹŻä»Ąç?†č§Łä¸şi += i & (-i)ć?Żĺ?‘ä¸Ščµ°ďĽŚç›´ĺ?°é€ščż‡ĺŹłć‹?é?‡ĺ?°çĄ–ĺ…?čŠ‚ç‚ąă€‚i -= i & (-i)ĺ?‘ä¸Ščµ°ďĽŚç›´ĺ?°é€ščż‡ĺ·¦ć‹?é?‡ĺ?°çĄ–ĺ…?čŠ‚ç‚ąďĽ?ćśŞčŻ?ć?ŽďĽ‰
# ĺą¶ä¸Ťć€»ć?Żć ‘ĺ˝˘ďĽŚćŻ”ĺ¦‚n=5ć—¶äĽšćś‰ä¸€ä¸ŞčŠ‚ç‚ąć?Żĺ?†ç¦»ć€?ďĽ?ĺ› ä¸ş6ć˛ˇĺŠ čż›ĺŽ»ďĽ‰ă€‚ä˝†ć?Żä¸Ťĺ¦¨ç˘Ťç®—ćł•čż?čˇŚă€‚
# čż™ä¸Şć•°ćŤ®ç»“ćž„ć˛ˇç”¨ć•°ç»„çš„ç¬¬0éˇąă€‚
# Fenwick Treeçš„ĺ…?ç´ ä¸Şć•°ć?Żĺ›şĺ®šçš„ďĽŚä¸Ťčż‡ĺŹŻä»ĄćŹ?ĺ‰ŤĺĽ„ä¸€ĺ †ä¸ş0çš„ĺ…?ç´ ćťĄć¨ˇć‹źĺŹ?ĺŚ–ďĽ?ĺ’Śä˝żç”¨ć•°ç»„ĺ?Ść ·é?“ç?†ďĽ‰ďĽŚç˝®0ä¸şĺŽ»é™¤ďĽŚ0ç˝®ĺ…¶ä»–ć•°ä¸şć·»ĺŠ 

FT=FenwickTree(5)
FT.add(0,1)
print(FT.bit)
print(FT.query(1,4))
