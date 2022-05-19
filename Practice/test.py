from sortedcontainers import SortedDict
import sortedcontainers
import collections


sd = SortedDict({"1": 1, "2": 2, "3": 3})
print(sd.peekitem(1))
