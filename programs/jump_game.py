""""
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

def jump_game(nums: list)-> bool:       # the target is the last index. It checks if the las index can be reached by the previos
    t = len(nums) - 1                   # index until indes 0, it there is a inde than can reachthe last, this index becames
    p = t - 1                           # the new target. If there isn´t a possible previous node then return False
    while p > -1 :
        if nums[p] >= (t - p) :
            if p == 0 :
                return True
            else :
                t = p
                p = t - 1
                continue
        else :
            p -= 1
    return False

def canJump(nums):                  # copoy from internet. It checks the 0 elements in the list, because is the only element
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