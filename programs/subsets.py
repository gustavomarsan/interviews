"""
https://leetcode.com/problems/subsets/
78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]

Use a backtracking always check 1 and 2 elements of the list and 
Once It have 2 elements, checks every one and add a element to the first one and No add to the other
Generating new 2 elements and backtracking the new 2 elements

programs/images/Subsets.png

"""

def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    partial = []

    def backtracking(i)-> list:
        if i == len(nums):
            result.append(partial[:])
            return

        partial.append(nums[i])
        backtracking(i+1)       

        partial.pop()
        backtracking(i+1)       
        
    backtracking(0)
    return result


nums = [1,2,3]

print(subsets(nums))

