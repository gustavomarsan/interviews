"""
https://leetcode.com/problems/house-robber/
198. House Robber
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
""" 
def rob(nums: list[int]) -> int:        # using a list for extra space
    if len(nums) == 1 :
        return nums[0]
    acum = [0] * len(nums)
    acum[0] = nums[0]
    acum[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)) :
        acum[i] = max(acum[i-1], acum[i-2]+nums[i])
    return acum[-1]

def rob_house(nums: list[int]) -> int :     # using 2 vars for extra space       **favorite**
    prev1 = prev2 = 0
    for num in nums :
        maximum = max(prev1, prev2+num)
        prev2 = prev1
        prev1 = maximum
    return maximum

a = [2,7,9,3,1]
print(rob(a))
print(rob_house(a))