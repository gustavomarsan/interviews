""" 
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
                   -             -     7 height x 7 wide
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""

def maxArea(height: list[int])-> int :
    left = 0
    volume = 0
    right = len(height) - 1
    while left < right :
        volume = max(volume, (right - left) * min (height[left], height[right]))
        if height[left] <= height[right] :
            p = left + 1
            while p <= right and height[p] <= height[left] :
                p += 1
            left = p
        else :
            p = right - 1
            while p >= left and height[p] <= height[right] :
                p -= 1
            right = p
    return volume

height = [1,9,6,2,5,1,8,3,7]
print(maxArea(height))