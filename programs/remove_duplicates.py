""""        
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element 
appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

"""

def removeDuplicates(nums):
    p1 = 2
    k = len(nums)
    while p1 < k :
        if nums[p1] == nums[p1-1] and nums[p1] == nums[p1-2] :
            k -= 1
            p2 = p1 
            temp = nums[p1]
            while p2 < len(nums) -1 :
                nums[p2] = nums[p2+1]
                p2 +=1
            nums[p2] = temp
        else :
            p1 += 1
            continue
    print(nums)
    return k
    

a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(a))
        