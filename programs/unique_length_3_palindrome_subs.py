"""
1930. Unique Length-3 Palindromic Subsequences
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
Constraints:
3 <= s.length <= 105
s consists of only lowercase English letters.
*** Note: create a set of letters of s, loop letter in letters, get index of first appear of letter (index())
and last appear (rindex()) in s.  Once we had indexes i an j iterate (K) between i and j create a set with k.
length of set k is number of diferent palindromes of 3 length for this letter (i , j)

"""


def countPalindromicSubsequence(s: str) -> int:
    letters = set(s)            # create a set of letter on s. max 26 items
    ans = 0
    for letter in letters :     
        i = s.index(letter)     # index of first element in s
        j = s.rindex(letter)    # index of last element in s
        between = set()         # create a set for elements between i an j

        for k in range(i + 1, j) :      
            between.add(s[k])
            
        ans += len(between)
    return ans


s = "bbcbaba"
print(countPalindromicSubsequence(s))