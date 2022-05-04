trans=[[1,2],[3,4]]
list(map(list,zip(*trans))) # matrix transformation using zip*

# create matrix without numpy
m=3
n=2
aa=[[0 for j in range(n)] for i in range(m)]