"""
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


def threeSum(nums):     # this method isn't efficient with time complexity. I will try a new one with 3 pointers
    results = []
    for p1 in range(len(nums) - 2) :
        target = 0 - nums[p1]
        my_set = set()
        for p2 in range (p1+1, len(nums)) :
            diff = target - nums[p2]
            if diff in my_set :
                one_result = [nums[p1], nums[p2], diff]
                one_result.sort()
                if one_result not in results : 
                    results.append(one_result)
                continue
            else :
                my_set.add(nums[p2])
    return results

a = [-1,0,1,2,-1,-4]
print(threeSum(a))