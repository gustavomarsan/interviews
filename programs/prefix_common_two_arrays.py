"""
2657. Find the Prefix Common Array of Two Arrays
https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.
A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
Example 1:
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.    # until index 0 no common number between A and B
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.       # until index 1 2 common numbers between A and B
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.   # until index 2 3 common numbers between A and B
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.# until index 3 4 common numbers between A and B
Example 2:
Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
Constraints:
1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
*** Note:  2 solutions
"""

# using sets for lists A every loop in read A and B and added to its sets
# double loop for checking if elements in set a arer in elements in set b to find common elements and adde to results
# O(n^2) because we have a loop inside a loop
def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
    set_a = set()
    set_b = set()
    result = [0] * len(A)
    for i in range(len(A)) :            # read A and B and add elements to its set
        set_a.add(A[i])
        set_b.add(B[i])
        common = 0
        for value in set_a :            # chek
            if value in set_b :
                common += 1
        result[i] = common
    return result

# O(n) complexity. Only one loop, but using extra space for set number of appareances of elements. If one elements appear mor than 1 time is added 1 to common and set to result
def findThePrefixCommonArray_2(A: list[int], B: list[int]) -> list[int]:
    result = [0] * len(A)
    frequency = [0] * (len(A) +1)
    common = 0
    for i in range(len(A)) :
        frequency[A[i]] += 1
        if frequency[A[i]] > 1 :
            common +=1
            
        frequency[B[i]] += 1
        if frequency[B[i]] > 1 :
            common +=1
            
        result[i] = common

    return result

a = [1,3,2,4]
b = [3,1,2,4]
print(findThePrefixCommonArray(a, b)) 
print(findThePrefixCommonArray_2(a, b)) 