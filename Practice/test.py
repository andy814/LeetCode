import math
from functools import cache
from itertools import combinations
from collections import Counter

counter1=Counter([1,1,2,4,5,7])
counter2=Counter([1,2,4,4,5,6])
counter3=counter1-counter2
print(counter3)
counter4=counter1+counter2
print(counter4)

counter1.subtract(counter2)
print(counter1)