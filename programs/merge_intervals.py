"""
https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def overlap(intervals: list[list[int]])-> list[list[int]] :
    intervals.sort()
    new_list = []
    for item in intervals:
        if new_list and item[0] <= new_list[-1][1] :
            new_list[-1][1] = max(item[1], new_list[-1][1])
        else : 
            new_list.append(item)
    return new_list      


intervals = [[1,4],[2,3]]
print(overlap(intervals))