"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start 
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval 
newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    new_list = []
    done = False
    open_int = False
    init = 0
    for interval in intervals :
        if not open_int and (done or newInterval[0] > interval[1]) :
            new_list.append(interval)
            continue
        elif not open_int and not done and newInterval[1] < interval[0] :
            done = True
            new_list.append(newInterval)
            new_list.append(interval)
        elif not open_int and newInterval[1] <= interval[1] :
            done = True
            new_list.append([min(interval[0], newInterval[0]), max(interval[1], newInterval[0])])
        elif not open_int and not done and newInterval[1] >= interval[1]:
            open_int = True
            init = min(interval[0], newInterval[0])
        elif open_int and interval[0] > newInterval[1] :
            new_list.append([init, max(newInterval[1], higher)])
            done =  True
            open_int = False
            new_list.append(interval)
            open_int = False
        higher = interval[1]
    if open_int :
        new_list.append([init, max(newInterval[1], higher)])
        done = True
    if not done :
        new_list.append(newInterval)
    return new_list



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
print(insert(intervals, newInterval))