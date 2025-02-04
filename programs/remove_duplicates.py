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
    i = 2  # i for index, begin in 2 because loop checks 2 previous index
    k = len(nums)
    while i < k :   
        if k < len(nums) :
            nums[i] = nums[i+len(nums) - k]  
        if nums[i] == nums[i-1] and nums[i] == nums[i-2] :  
            k -= 1
            if i < k : 
                nums[i] = nums[k]  
        else :
            i += 1  
    print(nums[:k])
    return k
    
def removeDuplicates_2(nums):
    repeated = 0
    for i in range(2, len(nums)):
        if nums[i] == nums[i-1] and nums[i] == nums[i-2] : 
            repeated += 1 
        elif repeated > 0 :
            nums[i-repeated] = nums[i]
            nums[i] = None
    print(nums[:len(nums)- repeated])
    return len(nums)-repeated


a = [1,1,1,2,2,2,3,3]
print(removeDuplicates(a))
print(removeDuplicates_2(a))
        