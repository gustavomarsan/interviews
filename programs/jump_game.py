""""
55. Jump Game
https://leetcode.com/problems/jump-game/
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def jump_game(nums: list)-> bool:       # the goal is the last index. It checks if the last index can be reached by the previos
    goal = len(nums) - 1                # index until index 0, it there is a index that can reach the last, this index becames
                                        # the new goal. At the end if goal = 0, it means last index can be reaches from 0 index
    for i in range(goal -1, -1, -1) :
        if nums[i] + 1 >= goal :
            goal = i
    return goal == 0

def canJump(nums):                  # copy from internet. It checks the 0 elements in the list, because is the only element
    mx, n = 0, len(nums)            # that not walks, if can skip the 0 element and finish the loop then it´s True
    for i in range(n):
        mx = max(mx, nums[i]+i)
        if nums[i] == 0:
            if i+1 == n: break
            if(mx == i): return False
    return True

a = [3, 0, 1, 1, 4]
print(canJump(a))
print(jump_game(a))