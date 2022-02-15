from collections import Counter
aa=[1,2]
bb=[1,2]
print(aa==bb) # True

aa=[1,2]
bb=[2,1]
print(aa==bb) # False

aa=Counter(aa)
bb=Counter(bb)
print(aa==bb) # True
print(list(aa.elements())) # [1,2]
print(list(bb.elements())) # [2,1]

print(tuple(aa.items()))