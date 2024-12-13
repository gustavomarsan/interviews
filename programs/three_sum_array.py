"""
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.  (<--- target)
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
*** Note:  is the same problem of findind 3 number to target sum = 0 
*** Shoulde solved with a loop and two pointers
"""

# wrong solution by using 2 loops. It runs but O(n^3) complexity
def threeSum(nums: list[int])-> list:     # this method isn't efficient with time complexity. I will try a new one with 3 pointers
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

# right solution using 1 loop and 2 pointers as slidng window. O(n^2) complexity
def threeSum2(nums: list[int])-> list:     # this method isn't efficient with time complexity. I will try a new one with 3 pointers
    results = []
    nums.sort()
    for i in range(len(nums) - 2) :
        if i > 0  and nums[i] == nums[i-1] :    # avoid repetead numbers in i
            continue
        p1 = i + 1 
        p2 = len(nums) -1
        while p1 < p2 :
            if nums[i] + nums[p1] + nums[p2] == 0 :
                results.append([nums[i], nums[p1], nums[p2]])
                p1 += 1
                while nums[p1] == nums[p1-1] and p1 < p2 :  # avoid repeated p1
                    p1 += 1
            elif nums[i] + nums[p1] + nums[p2] > 0 :
                p2 -= 1
                while nums[p2] == nums[p2+1] and p1 < p2 :  # avoid repeated p2
                    p2 -= 1
            else :
                p1 += 1
                while nums[p1] == nums[p1-1] and p1 < p2 :  # avoid repeated p1
                    p1 += 1
    return results


a = [-1,0,1,2,-1,-4]
b = [0,1,1]
c = [0,0,0,0]
print(threeSum(a))
print(threeSum(b))
print(threeSum(c))
print(threeSum2(a))
print(threeSum2(b))
print(threeSum2(c))