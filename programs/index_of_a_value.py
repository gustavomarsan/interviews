"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

It is found
Input: nums = [1,3,5,6], target = 5
Output: 2

It is not found
Input: nums = [1,3,5,6], target = 2
(a, b, m)
 0  3  1
 0  0  0
 0 -> 1
 
 ans: 1
 
 (a, b, m) t = 4
  0. 3  1
  2. 3. 2
  2. 1. -
  m + 1
  ans: 2
  -> m -1
 
 (a, b, m) t = f
  0. 3  1
  2. 3. 2
  3. 3. 
 

Output: 1
"""

def find_index(numbers: list[int], target: int) -> int :
  a = 0
  b = len(numbers) - 1
  while a < b :
    m = (b + a) // 2
    if target <= numbers[a] :                #check if value if lower or equal to numbers[a]
        return a
    if target >= numbers[b] :                # check if value is greater or equal to numbers[b]
        return b if target == numbers[b] else b + 1
    if numbers[m] == target :
        return m
    if target > numbers[m]:
      a = m + 1
    else :
      b = m - 1
    
  return m if numbers[m] > target  else m + 1

a = [3,5,7,10]
print(find_index(a, 4))