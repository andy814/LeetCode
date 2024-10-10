# create matrix without numpy
m=3
n=2
aa=[[0 for j in range(n)] for i in range(m)]

# 90度旋转
matrix=[[1,2,3],[4,5,6],[7,8,9]]

# 顺时针：先上下翻转后转置
# reverse top to bottom then transpose
matrix[:] = list(map(list,zip(*matrix[::-1])))

# 逆时针：先转置后上下翻转
matrix[:] = list(map(list,zip(*matrix)))[::-1]

# 转置：
# zip(*matrix) 就是求转置，只不过每一个元素都是tuple，需要用map把每一个元组转换成list
matrix[:] = list(map(list,zip(*matrix)))


# pre-compute prefix sum
# source: https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75448/Sharing-My-Python-solution
class NumMatrix:
      def __init__(self, matrix):
          if not matrix:
              return
          n, m = len(matrix), len(matrix[0])
          self.sums = [ [0 for j in range(m+1)] for i in range(n+1) ]
          for i in range(1, n+1):
              for j in range(1, m+1): # add an extra row and column to simplify the logic here
                  self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]
    

      def sumRegion(self, row1, col1, row2, col2):
          row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
          return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]