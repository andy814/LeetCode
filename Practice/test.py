import math
from functools import cache
from itertools import combinations

@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(100))