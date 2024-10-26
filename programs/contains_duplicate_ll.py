""""
https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Note : in dicts but only need to store un the dict the last apereance of the number, example
nums = [1,0,1,1] when add 1 to dict,   my_set = {1: 0} then in the next 1  change to {1: 2, 0: 1}, we only need to update 
repeated number
"""

def containsNearbyDuplicate(nums: list[int], k: int)-> bool:
    my_dict = {}
    for i in range(len(nums)) :
        if nums[i] in my_dict and i - my_dict[nums[i]] <= k :
            return True
        else :
            my_dict[nums[i]] = i
    return False

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))
