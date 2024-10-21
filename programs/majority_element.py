"""""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists 
in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

assumen that always there is a majotity element in the list

"""

def majority_element(nums: list) -> int :
    num = 0
    max = 0
    for n in nums :
        if max == 0 :
            num = n
        if n == num :
            max += 1
        else : 
            max -= 1
    return num

a = [1, 1, 1, 2, 2, 2, 2 ]
print(majority_element(a))