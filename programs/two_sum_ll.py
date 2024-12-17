"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they 
add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
***** Keys : Ordered list. No extra space shoul be used ****
"""

def two_sum(numbers:list[int] , target: int)-> list[int]:
    p1 = 0
    p2 = 1
    up = True       # it control if it is posible to continue growing p2. when sum > target it is imposible to grow p2
    while True :
        sum = numbers[p1] + numbers[p2]
        if sum == target :
            return[p1+1, p2+1]
        elif sum > target :       # decrease p2 
            p2 -= 1
            up = False      # no more grow up p2
        elif up and p2 < len(numbers) - 1 :
            p2 += 1
        else :          #when we just can grow up p1 to reach the index
            p1 += 1
    return

def two_sum2(numbers:list[int] , target: int)-> list[int]:
    p1 = 0
    p2 = len(numbers) -1
    while p1 < p2 :
        sum = numbers[p1] + numbers[p2]
        if sum == target :
            return[p1+1, p2+1]
        elif sum > target :       # decrease p2 
            p2 -= 1
        else :          #when we just can grow up p1 to reach the index
            p1 += 1
        

numbers = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
print(two_sum(numbers, 542))
print(two_sum2(numbers, 542))