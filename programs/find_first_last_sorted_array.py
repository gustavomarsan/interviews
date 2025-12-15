"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""


def searchRange(nums: list[int], target: int) -> list[int]:
    ini = 0
    fin = len(nums)-1
    while ini <= fin:      # search for the target with binary search
        point =  (ini + fin) // 2
        if nums[point] == target:
            #if found, search for target neighbors
            first = point
            last = point
            while first > 0 and nums[first-1] == target:
                first -= 1
            while last < len(nums) -1 and nums[last+1] == target:
                last += 1
            return first, last

        elif nums[point] > target:
            fin = point -1
        else:
            ini = point +1

    return -1, -1       #target not found

#bqcx-974850199516-c23a@gcp-sa-bigquery-condel.iam.gserviceaccount.com

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]