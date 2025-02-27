"""
1749. Maximum Absolute Sum of Any Subarray
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
**** Note: Taken from editorial
Complexity O(n)
"""
#solution og editorial. It works but I don´t know why
def maxAbsoluteSum(nums: list[int]) -> int:
    curr_sum = 0
    max_sum = 0
    min_sum = 0
    for num in nums :
        curr_sum += num
        if curr_sum > max_sum :
            max_sum = curr_sum
        if curr_sum < min_sum :
            min_sum = curr_sum
    return max_sum - min_sum

#my solution. Similar to maximum array but having 2 maximum values.The higher and de lower. Returning max abs
def maxAbsoluteSum_2(nums: list[int]) -> int:
    curr_posi = 0
    curr_nega = 0
    max_posi = 0
    max_nega = 0
    for num in nums :
        curr_posi = max(curr_posi + num, num)
        curr_nega = min(curr_nega + num, num)
        max_posi = max(max_posi, curr_posi)
        max_nega = min(max_nega, curr_nega)
    return max(max_posi, abs(max_nega))



nums =  [1,-3,2,3,-4]
print(maxAbsoluteSum(nums))
print(maxAbsoluteSum_2(nums))