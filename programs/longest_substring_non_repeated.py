"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def lengthOfLongestSubstring(s: str) -> int:
    p1 = 0
    p2 = 0
    max_len = 0
    my_set = set()
    while p2 < len(s) :
        if s[p2] in my_set :
            my_set.remove(s[p1])
            p1 += 1
            continue
        my_set.add(s[p2])
        max_len = max(max_len, len(my_set))
        p2 +=1
    return max_len

s = "abcabb"
print(lengthOfLongestSubstring(s))
                
        