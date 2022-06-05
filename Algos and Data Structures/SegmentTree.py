from math import ceil, log2
import sys


# source: https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/python-well-commented-solution-using-segment-trees
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            
            return root.total
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j): # inclusive!
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)
                


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,3,2,5,4])
print(numArray.sumRange(0, 1))
numArray.update(1, 10)
print(numArray.sumRange(1, 2))







#------------------------------------------------------------------------------------------
# Source: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/?ref=lbp
# Segment Tree - Sum of given range - without lazy propagation
# Note that queries are inclusive, 0-indexed


# A utility function to get the
# middle index from corner indexes.
# 用update实现build_tree是可行的
# 注意总共存在两套坐标系统：arr和i对应实际数组，st和si对应线段树中储存的数组，ss,se,qs,qe对应实际数组的范围
def getMid(s, e) :
    return s + (e -s) // 2
 
""" A recursive function to get the sum of values
    in the given range of the array. The following
    are parameters for this function.
 
    st --> Pointer to segment tree
    si --> Index of current node in the segment tree.
           Initially 0 is passed as root is always at index 0
    ss & se --> Starting and ending indexes of the segment
                represented by current node, i.e., st[si]
    qs & qe --> Starting and ending indexes of query range """
def getSumUtil(st, ss, se, qs, qe, si) :
 
    # If segment of this node is a part of given range,
    # then return the sum of the segment
    if (qs <= ss and qe >= se) :
        return st[si]
 
    # If segment of this node is
    # outside the given range
    if (se < qs or ss > qe) :
        return 0
 
    # If a part of this segment overlaps
    # with the given range
    mid = getMid(ss, se)
     
    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + \
           getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2)
 
""" A recursive function to update the nodes
which have the given index in their range.
The following are parameters st, si, ss and se
are same as getSumUtil()
i --> index of the element to be updated.
      This index is in the input array.
diff --> Value to be added to all nodes
which have i in range """
def updateValueUtil(st, ss, se, i, diff, si) :
 
    # Base Case: If the input index lies
    # outside the range of this segment
    if (i < ss or i > se) :
        return
 
    # If the input index is in range of this node,
    # then update the value of the node and its children
    st[si] = st[si] + diff
     
    if (se != ss) :
     
        mid = getMid(ss, se)
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1)
        updateValueUtil(st, mid + 1, se, i,
                         diff, 2 * si + 2)
 
# The function to update a value in input array
# and segment tree. It uses updateValueUtil()
# to update the value in segment tree
# set the value to new_val
def updateValue(arr, st, n, i, new_val) :
 
    # Check for erroneous input index
    if (i < 0 or i > n - 1) :
         
        print("Invalid Input", end = "")
        return
 
    # Get the difference between
    # new value and old value
    diff = new_val - arr[i]
 
    # Update the value in array
    arr[i] = new_val
 
    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, diff, 0)
 
# Return sum of elements in range from
# index qs (query start) to qe (query end).
# It mainly uses getSumUtil()
def getSum(st, n, qs, qe) : # qs and qe are inclusive!
 
    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe) :
 
        print("Invalid Input", end = "")
        return -1
     
    return getSumUtil(st, 0, n - 1, qs, qe, 0)
 
# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :
 
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se) :
     
        st[si] = arr[ss]
        return arr[ss]
     
    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = getMid(ss, se)
     
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + \
             constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
     
    return st[si]
 
""" Function to construct segment tree
from given array. This function allocates memory
for segment tree and calls constructSTUtil() to
fill the allocated memory """
def constructST(arr, n) :
 
    # Allocate memory for the segment tree
 
    # Height of segment tree
    x = (int)(ceil(log2(n)))
 
    # Maximum size of segment tree
    max_size = 2 * (int)(2**x) - 1
     
    # Allocate memory
    st = [0] * max_size
 
    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0)
 
    # Return the constructed segment tree
    return st
 

# Driver Code for sum query without postpone propagation
if __name__ == "__main__" :
 
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
 
    # Build segment tree from given array
    st = constructST(arr, n)
 
    # Print sum of values in array from index 1 to 3
    print("Sum of values in given range = ",
                       getSum(st, n, 1, 3))
 
    # Update: set arr[1] = 10 and update
    # corresponding segment tree nodes
    updateValue(arr, st, n, 1, 10)
 
    # Find sum after the value is updated
    print("Updated sum of values in given range = ",
                     getSum(st, n, 1, 3), end = "")


#------------------------------------------------------------------------------------------
# Source: https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/?ref=lbp
# Segment Tree - range minimum query - without lazy propagation
# Note that queries are inclusive, 0-indexed

# Python3 program for range minimum
# query using segment tree
INT_MAX = sys.maxsize

# A utility function to get
# minimum of two numbers
def minVal(x, y) :
	return x if (x < y) else y

# A utility function to get the
# middle index from corner indexes.
def getMid(s, e) :
	return s + (e - s) // 2

""" A recursive function to get the
minimum value in a given range
of array indexes. The following
are parameters for this function.

	st --> Pointer to segment tree
	index --> Index of current node in the
		segment tree. Initially 0 is
		passed as root is always at index 0
	ss & se --> Starting and ending indexes
				of the segment represented
				by current node, i.e., st[index]
	qs & qe --> Starting and ending indexes of query range """
def RMQUtil( st, ss, se, qs, qe, index) :

	# If segment of this node is a part
	# of given range, then return
	# the min of the segment
	if (qs <= ss and qe >= se) :
		return st[index]

	# If segment of this node
	# is outside the given range
	if (se < qs or ss > qe) :
		return INT_MAX

	# If a part of this segment
	# overlaps with the given range
	mid = getMid(ss, se)
	return minVal(RMQUtil(st, ss, mid, qs,
						qe, 2 * index + 1),
				RMQUtil(st, mid + 1, se,
						qs, qe, 2 * index + 2))

# Return minimum of elements in range
# from index qs (query start) to
# qe (query end). It mainly uses RMQUtil()
def RMQ( st, n, qs, qe) :

	# Check for erroneous input values
	if (qs < 0 or qe > n - 1 or qs > qe) :
	
		print("Invalid Input")
		return -1
	
	return RMQUtil(st, 0, n - 1, qs, qe, 0)

# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :

	# If there is one element in array,
	# store it in current node of
	# segment tree and return
	if (ss == se) :

		st[si] = arr[ss]
		return arr[ss]

	# If there are more than one elements,
	# then recur for left and right subtrees
	# and store the minimum of two values in this node
	mid = getMid(ss, se)
	st[si] = minVal(constructSTUtil(arr, ss, mid,
									st, si * 2 + 1),
					constructSTUtil(arr, mid + 1, se,
									st, si * 2 + 2))
	
	return st[si]

"""Function to construct segment tree
from given array. This function allocates
memory for segment tree and calls constructSTUtil()
to fill the allocated memory """
def constructST( arr, n) :

	# Allocate memory for segment tree

	# Height of segment tree
	x = (int)(ceil(log2(n)))

	# Maximum size of segment tree
	max_size = 2 * (int)(2**x) - 1

	st = [0] * (max_size)

	# Fill the allocated memory st
	constructSTUtil(arr, 0, n - 1, st, 0)

	# Return the constructed segment tree
	return st

#------------------------------------------------------------------------------------------
# Source: https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/?ref=lbp
# Segment Tree - sum of given range - with lazy propagation
# Note that queries are inclusive, 0-indexed

# Python3 implementation of the approach
MAX = 1000
 
# Ideally, we should not use global variables
# and large constant-sized arrays, we have
# done it here for simplicity.
tree = [0] * MAX # To store segment tree
lazy = [0] * MAX # To store pending updates
 
""" si -> index of current node in segment tree
    ss and se -> Starting and ending indexes of elements
                for which current nodes stores sum.
    us and ue -> starting and ending indexes of update query
    diff -> which we need to add in the range us to ue """
def updateRangeUtil(si, ss, se, us, ue, diff) :
 
    # If lazy value is non-zero for current node
    # of segment tree, then there are some
    # pending updates. So we need to make sure
    # that the pending updates are done before
    # making new updates. Because this value may be
    # used by parent after recursive calls
    # (See last line of this function)
    if (lazy[si] != 0) :
         
        # Make pending updates using value
        # stored in lazy nodes
        tree[si] += (se - ss + 1) * lazy[si]
 
        # checking if it is not leaf node because if
        # it is leaf node then we cannot go further
        if (ss != se) :
         
            # We can postpone updating children we don't
            # need their new values now.
            # Since we are not yet updating children of si,
            # we need to set lazy flags for the children
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]
         
        # Set the lazy value for current node
        # as 0 as it has been updated
        lazy[si] = 0
     
    # out of range
    if (ss > se or ss > ue or se < us) :
        return 
 
    # Current segment is fully in range
    if (ss >= us and se <= ue) :
         
        # Add the difference to current node
        tree[si] += (se - ss + 1) * diff
 
        # same logic for checking leaf node or not
        if (ss != se) :
         
            # This is where we store values in lazy nodes,
            # rather than updating the segment tree itself
            # Since we don't need these updated values now
            # we postpone updates by storing values in lazy[]
            lazy[si * 2 + 1] += diff
            lazy[si * 2 + 2] += diff
         
        return
 
    # If not completely in rang, but overlaps,
    # recur for children,
    mid = (ss + se) // 2
    updateRangeUtil(si * 2 + 1, ss,
                    mid, us, ue, diff)
    updateRangeUtil(si * 2 + 2, mid + 1,
                    se, us, ue, diff)
 
    # And use the result of children calls
    # to update this node
    tree[si] = tree[si * 2 + 1] + \
            tree[si * 2 + 2]
 
# Function to update a range of values
# in segment tree
 
''' us and eu -> starting and ending indexes
                of update query
    ue -> ending index of update query
    diff -> which we need to add in the range us to ue '''
# note that the last parameter is diff, which means the value we add for all elements in the range 
def updateRange(n, us, ue, diff) :
    updateRangeUtil(0, 0, n - 1, us, ue, diff)
 
''' A recursive function to get the sum of values
    in given range of the array. The following are
    parameters for this function.
    si --> Index of current node in the segment tree.
        Initially 0 is passed as root is always at'
        index 0
    ss & se --> Starting and ending indexes of the
                segment represented by current node,
                i.e., tree[si]
    qs & qe --> Starting and ending indexes of query
                range '''
def getSumUtil(ss, se, qs, qe, si) :
 
    # If lazy flag is set for current node
    # of segment tree, then there are
    # some pending updates. So we need to
    # make sure that the pending updates are
    # done before processing the sub sum query
    if (lazy[si] != 0) :
     
        # Make pending updates to this node.
        # Note that this node represents sum of
        # elements in arr[ss..se] and all these
        # elements must be increased by lazy[si]
        tree[si] += (se - ss + 1) * lazy[si]
 
        # checking if it is not leaf node because if
        # it is leaf node then we cannot go further
        if (ss != se) :
         
            # Since we are not yet updating children os si,
            # we need to set lazy values for the children
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]
 
        # unset the lazy value for current node
        # as it has been updated
        lazy[si] = 0
 
    # Out of range
    if (ss > se or ss > qe or se < qs) :
        return 0
 
    # At this point we are sure that
    # pending lazy updates are done for
    # current node. So we can return value
    # (same as it was for query in our previous post)
 
    # If this segment lies in range
    if (ss >= qs and se <= qe) :
        return tree[si]
 
    # If a part of this segment overlaps
    # with the given range
    mid = (ss + se) // 2
    return (getSumUtil(ss, mid, qs, qe, 2 * si + 1) +
            getSumUtil(mid + 1, se, qs, qe, 2 * si + 2))
 
# Return sum of elements in range from
# index qs (query start) to qe (query end).
# It mainly uses getSumUtil()
def getSum(n, qs, qe) :
     
    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe) :
        print("Invalid Input")
        return -1
 
    return getSumUtil(0, n - 1, qs, qe, 0)
 
# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment
# tree st.
def constructSTUtil(arr, ss, se, si) :
 
    # out of range as ss can never be
    # greater than se
    if (ss > se) :
        return 
 
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se) :
     
        tree[si] = arr[ss]
        return
     
    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = (ss + se) // 2
    constructSTUtil(arr, ss, mid, si * 2 + 1)
    constructSTUtil(arr, mid + 1, se, si * 2 + 2)
 
    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]
 
''' Function to construct segment tree
from given array. This function allocates memory
for segment tree and calls constructSTUtil()
to fill the allocated memory '''
def constructST(arr, n) :
     
    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, 0)
     



# source: https://leetcode.com/problems/booking-concert-tickets-in-groups/discuss/2084171/Python-segment-tree-to-query-sum-and-lowest-index.
# Segment Tree for sumRange and MaxNbr
class SegmentTree():
    def __init__(self, l, r):
        self.val = 0
        self.mid = (l + r) // 2
        self.l = l
        self.r = r
        self.left, self.right = None, None
        self.max = 0
        self.sums = 0
        if l != r:
            self.left = SegmentTree(l, self.mid)
            self.right = SegmentTree(self.mid + 1, r)

    def update(self, l, r, val=1):
        if self.l >= l and self.r <= r:
            self.val += val
            self.max += val
            self.sums += val*(r-l+1)
            return
        if self.l > r or self.r < l:
            return

        self.left.update(l, r, val)
        self.right.update(l, r, val)
        self.max = self.val + max(self.left.max, self.right.max)
        self.sums = self.val*(self.r-self.l+1)+self.left.sums+self.right.sums

    def query(self, i):
        if self.l == self.r and self.l == i:
            return self.val
        if i < self.l or i > self.r:
            return 0
        if i <= self.mid:
            return self.val + self.left.query(i)
        return self.val + self.right.query(i)
    
    def querySum(self,l,r):
        #return sum value in range [l,r]
        if self.l >= l and self.r <= r:
            return self.sums
        if self.l > r or self.r < l:
            return 0
        return self.val*(min(r,self.r)-max(l,self.l)+1)+self.left.querySum(l,r)+self.right.querySum(l,r)

    def queryLowestGreater(self,v):
        #return the smallest row that remain seats greater than v
        if self.max<v:
            return -1
        if self.l == self.r:
            return -1 if self.max<v else self.l
        if self.left.max >= v-self.val:
            return self.left.queryLowestGreater(v-self.val)
        return self.right.queryLowestGreater(v-self.val)

