import numpy as np
'''
aa=[ [1,2,3],[4,5,6],[7,8,9] ]
aa[:][0]=[100,200,300]
print(aa)
print(aa[:][0])

aa=[ [1,2,3],[4,5,6],[7,8,9] ]
aa[0][1:]=[200,300]
print(aa)

aa=[ [1,2,3],[4,5,6],[7,8,9] ]
firstLine=aa[0][:]
firstLine=[100,200,300]
print(aa)

aa=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
aa[:,1]=[100,200,300]
print(aa)

aa=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
firstLine=aa[0,:]
firstLine=[100,200,300]
print(aa)

aa[-1]=[111,200,300]
print(aa)
'''

aa=[ [1,2,3],[4,5,6],[7,8,9] ]
line=aa[:][-1]
aa[:][-1]=[100,200,300]
print(line)

aa=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
line=aa[:,-1]
aa[:,-1]=[100,200,300]
print(line)

aa=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
firstLine=aa[0,:]
#firstLine[:]=[100,200,300]
aa[0,:]=[100,200,300]
print(aa)
print("line",firstLine)

aa=[ [1,2,3],[4,5,6],[7,8,9] ]
firstLine=aa[0][:]
#firstLine[:]=[100,200,300]
aa[0][:]=[100,200,300]
print(aa)
print("line",firstLine)

aa=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
firstLine=aa[0,:]
firstLine=[100,200,300]
print(aa)

