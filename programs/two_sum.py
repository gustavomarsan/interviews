"""
https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

[2, 3, 4]
       *
target = 6
dict_nums = {2 : 0, 3: 1}
i = 2
diff = 2  
(0, 2)
"""

def twoSum(nums: list[int], target: int)-> list[int]:
    dict_nums = {}
    for i in range(len(nums)) :
        diff = target - nums[i]
        if diff in dict_nums :
            return[dict_nums[diff], i]
        dict_nums[nums[i]] = i
    return None

nums = [2, 3, 4] 
target = 6
print(twoSum(nums, target))