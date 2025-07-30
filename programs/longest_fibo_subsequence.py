"""
873. Length of Longest Fibonacci Subsequence
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
A sequence x1, x2, ..., xn is Fibonacci-like if:
n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:
Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
Constraints:
3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109
***Note:  First make a set with the list. 
Then make a double loop (i,j) check 2 elements and search for a fibo sequ (i+j=k). if k in set there is a dibo seq
Finally do a while loop to searh a next fibo seq fromthe last tu numbers (j ,k)
Complexiti O(n^3)    -> n for i * n for j  * n for last while loop
"""
def lenLongestFibSubseq(arr: list[int]) -> int:
    my_set = set(arr)
    max_sub = 0
        
    for i in range(len(arr)- 2) :
        for j in range(i + 1, len(arr) - 1) :
            ans = 2
            n = arr[i]
            c = arr[j]
            k = n + c
            while k in my_set :
                ans += 1
                n, c  = c, k
                k = n + c
                if ans > max_sub :
                    max_sub = ans
                #max_sub = max(max_sub, ans)
    return max_sub if max_sub != 2 else 0

nums = [1,2,3,4,5,6,7,8]
print(lenLongestFibSubseq(nums))
