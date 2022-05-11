# create matrix without numpy
m=3
n=2
aa=[[0 for j in range(n)] for i in range(m)]

# 90度旋转
matrix=[[1,2,3],[4,5,6],[7,8,9]]

# 顺时针：
matrix[:] = list(map(list,zip(*matrix[::-1])))

# 逆时针：
matrix[:] = list(map(list,zip(*matrix)))[::-1]

# 转置：
matrix[:] = list(map(list,zip(*matrix)))


# zip(*matrix) 就是求转置，只不过每一个元素都是tuple，需要用map把每一个元组转换成list