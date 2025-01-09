"""



"""


def backtracking(nums: list[int], partial: list[int], result: list[list[int]]) -> list[list[int]] :
    # exit
    if len(partial) == len(nums) :      # when partial reach size append to result
        result.append(list(partial))
        return result
        
    # backtracking
    for num in nums :
        if num not in partial :             # this check is O(n) complexity each loop
            partial.append(num)
            backtracking(nums, partial, result)
            partial.pop()
    return result


def permute(nums: list[int]) -> list[list[int]]:    # option 1 using backtracking but check every loop if num in partial is O(n)

    return backtracking(nums, [], [])

def permute2(nums: list[int]) -> list[list[int]]:       # option 2, more 
    def backtrack(start) :
        if start == len(nums) :
            res.append(list(nums))
            return
        
        for i in range(start, len(nums)) :
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            
    res = []
    backtrack(0)
    return res


a = [1,2,3]
print(permute(a))
print(permute2(a))