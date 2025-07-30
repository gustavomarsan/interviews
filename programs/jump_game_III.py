"""
1306. Jump Game III
https://leetcode.com/problems/jump-game-iii/
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, 
you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
Notice that you can not jump outside of the array at any time.
Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
Constraints:
1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
*** Note: Solved using BFS and checking neighbors and add visited in a set, if neighbor have already visited not check again
else check and his neighbors too. If found value = 0 return True, else if no more neighbors to visit loop finish return false. 
"""


from collections import deque
def canReach(arr: list[int], start: int) -> bool:
    visited = set()
    visited.add(start)
    neighbors = deque([start])
    while neighbors :
        new_index = neighbors.popleft()
        if arr[new_index] == 0 :
            return True
        if new_index + arr[new_index] < len(arr) and new_index + arr[new_index] not in visited:
            neighbors.append(new_index + arr[new_index])
            visited.add(new_index + arr[new_index])
        if new_index - arr[new_index] > -1 and new_index - arr[new_index] not in visited:
            neighbors.append(new_index - arr[new_index])
            visited.add(new_index - arr[new_index])
    return False

nums = [3,0,2,1,2]    # start 2 = False 
nums2 = [4,2,3,0,3,1,2] # start 0 = True
print(canReach(nums2, 0))