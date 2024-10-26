"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
n = 4
k = 2

nums = [1,  2,  3,  4]
                    b()
                



partial= [ ]
results = [[1, 2], [1, 3],[ 1, 4],[2, 3], [2, 4], [3, 4]]
previus = 3
"""

def backtracking(nums, results, partial, k) :
    if len(partial) == k :
        results.append(list(partial))
        return
    
    for item in nums :
        if len(partial) == 0  or item > partial[-1] :
            partial.append(item)
            backtracking(nums, results, partial, k)
            partial.pop()
    
def combine(n, k):
    nums = [x for x in range(1, n+1)]
    if  k == n :
        return [nums]
    results = []
    backtracking(nums, results, [], k)
    return results

n = 8
k = 3
print(combine(n, k))