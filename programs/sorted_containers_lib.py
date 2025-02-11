"""
use of sortedcontainer lib
"""

from sortedcontainers import SortedList, SortedSet, SortedDict 

nums_set = SortedSet()
nums_set.add(9)
nums_set.add(4)
nums_set.add(2)
nums_set.add(8)
nums_set.add(11)
nums_set.add(3)
nums_set.add(5)
nums_set.add(1)
print(nums_set)
nums_set.remove(4)      # remove = discard
nums_set.discard(7)
nums_set.pop(0)
print(nums_set)
my_list = [4, 12, 3, 6, 8, 12, 9, 1]
nums_set.update(my_list)
print(nums_set)