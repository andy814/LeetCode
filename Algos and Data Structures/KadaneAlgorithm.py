# source: https://www.interviewbit.com/blog/maximum-subarray-sum/#:~:text=Kadane's%20Algorithm%20is%20an%20iterative,ending%20at%20the%20previous%20position.
# find the maximum sum of an subarray in O(n)
def maximumSubarraySum(arr):
       n = len(arr)
       maxSum = -float("inf")
       currSum = 0

       for i in range(n):
           currSum = currSum + arr[i]
           if(currSum > maxSum):
               maxSum = currSum
           if(currSum < 0):
               currSum = 0
      
       return maxSum