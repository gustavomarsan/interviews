"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

"""

def search(self, nums: list[int], target: int) -> int:
    ini = 0
    fin = len(nums) -1
    while ini <= fin:
        mid = (ini + fin) // 2
        if nums[mid] == target:
            return mid

        if nums[ini] <= nums[mid]:  #check if left side is sorted
            if nums[ini] <= target < nums[mid]:          # do the binary search in the left side
                fin = mid - 1
            else: 
                ini = mid + 1
        else:                      #right side is sorted
            if nums[mid] < target <= nums[fin]:         # do the binary search in the right side  
                ini = mid + 1
            else:
                fin = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(None, nums, target))  # Output: 4
