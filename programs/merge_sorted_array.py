"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be 
ignored. nums2 has a length of n.
note: in site of nums1 not in a new array

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

"""
 
def merge(nums1: list, m: int, nums2: list, n: int)-> list :
    p1 = m - 1
    p2 = n - 1
    p = m + n -1
    while p1 > -1 or p2 > -1 :
        if p2 == -1 or nums1[p1] > nums2[p2] and p1 > -1:      # move from nums1
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
        else : 
            nums1[p] = nums2[p2]
            p2 -=1
            p -= 1
    print(nums1)

    return 
   
        
a = [0]
b = [1]
        
merge(a, 0, b, 1)
            