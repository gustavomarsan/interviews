"""
https://leetcode.com/problems/permutations/description/

"""


def backtrack(nums: list[int], results, partial: list[int]) -> None :
    if len(nums) == len(partial) :
        results.append([item for item in partial])
        return
    
    for item in nums :
    	if item not in partial :
            partial.append(item) 
            backtrack(nums, results, partial)
            partial.pop()
    return results

def permutations(nums: list[int])-> list[list[int]] :
    results = []
    return backtrack(nums, results, [])


nums = [1, 2, 3]
print(permutations(nums))