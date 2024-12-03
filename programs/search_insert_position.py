"""
https://leetcode.com/problems/search-insert-position/
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
def searchInsert(nums: list[int], target: int)-> int:
    p1 = 0
    p2 = len(nums) - 1
    while p1 <= p2 :
        mid = (p1 + p2) // 2
        if nums[mid] < target :
             p1 = mid + 1
        elif nums[mid] > target :
            p2 = mid - 1
        else :
            return mid
    return p1    
        

nums = [1, 2, 3, 5, 6]
target = 6
print(searchInsert(nums, target))