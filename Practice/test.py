from itertools import combinations

def P1(ele):
    return ele+1

def equals1(ele):
    return ele==1

print(map(equals1,[1,2,3,4,5]))
print(list(map(P1,[1,2,3,4,5])))
print(list(combinations([1,2,3,4],2)))