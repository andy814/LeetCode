from itertools import product

aa=[tuple("()")]*2
result=product(*aa)
for i in result:
    print(i)