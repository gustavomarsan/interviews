"""
1726. Tuple with Same Product
https://leetcode.com/problems/tuple-with-same-product/
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d 
where a, b, c, and d are elements of nums, and a != b != c != d.
Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 10^4
All elements in nums are distinct.
Note: for serac of 4 indexes 
Brute force = 4 nested loops.  Complexity O(n^4)
Other option =  3 nested loops. + searc in hash
Optimal   is next solution
"""

# Optimal solution for high constrains
# precompute products
# nums = [2, 3, 4, 6]
# pairProducts = [6, 8, 12, 12, 18, 24]  repeated valus * 8  if it repeats morethan 3 inn a row is exponential
#  this solution is  O(n^2 log n)

def tupleSameProduct(nums: list[int]) -> int:
    def pairs_comb(l: int) -> int :
        pairs = 0
        while l > 0 :
            pairs += l
            l -=1
        return pairs
    
    nums.sort()
    l = len(nums)
    pairs = pairs_comb(l-1)
    pair_products = [0 for _ in range(pairs)]   # create pair_products list
    i = 0                                       #  i  or index on pair product_list
    for a in range(l-1) :                       # fill  pair_products list
        for b in range(a+1, l):
            pair_products[i] = (nums[a] * nums[b])
            i += 1
    pair_products.sort()
    last = 0
    repeated = 0
    consecutive = 0
    for pair in pair_products :
        if pair == last :
            repeated += 1 + consecutive
            consecutive +=1
        else :
            consecutive = 0
        last = pair
        

    return repeated * 8 
                            
# nums = [2,3,4,6]
nums = [1,2,4,5,10]
print(tupleSameProduct(nums))

