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
# it allows 2 elements per list
def removeDuplicates(nums):
    i = 2  # i for index, begin in 2 because loop checks 2 previous index
    active = len(nums)
    while i < active :   
        eliminated = len(nums) - active
        if eliminated > 0 :     # move elements each loop if there is eliminated values
            nums[i] = nums[i+ eliminated]  
        if nums[i] == nums[i-1] and nums[i] == nums[i-2] :      # don't ibcrease index i
            active -= 1
        else :
            i += 1  
    print(nums[:active])
    return active

# it allows 1 elements per list
def removeDuplicates_1(nums):
    i = 1  # i for index, begin in 1 because loop checks 1 previous index
    active = len(nums)
    while i < active :   
        eliminated = len(nums) - active
        if eliminated > 0 :     # move elements each loop if there is eliminated values
            nums[i] = nums[i+ eliminated]  
        if nums[i] == nums[i-1] :            # don't ibcrease index i
            active -= 1
        else :
            i += 1  
    print(nums[:active])
    return active



a = [1,1,1,1,2,2,2,2,3,3,3,3]
b = [1,1,1,2,2,2,3,3]
print(removeDuplicates(a))
print(removeDuplicates_1(b))
        