"""
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

My solution the same binary search used in Search in Rotated Sorted Array with a small modification to handle duplicates (rellocate pointers), by checking if ini pointer has the same value 
as its right neighbor then relocate it, and if fin pointer has the same value as their left neighbor then relocate it.
"""


def search(self, nums: list[int], target: int) -> bool:
    ini = 0
    fin = len(nums) -1
    while ini <= fin:
        #rellocate ini pointer if it has the same value as its right neighbor
        while fin > 0 and nums[fin-1] == nums[fin]:
            fin -=1
        #rellocate fin pointer if it has the same value as its left neighbor
        while ini < len(nums)-2 and nums[ini+1] == nums[ini]:
            ini += 1

        mid = (ini + fin) // 2
        if nums[mid] == target:
            return True

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
    return False


nums = [4,4,4,5,6,7,0,1,2]
target = 8
print(search(None, nums, target))  # Output: False





