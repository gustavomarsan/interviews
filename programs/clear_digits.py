"""
3174. Clear Digits
https://leetcode.com/problems/clear-digits/
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.
Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".
Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
Note: solutions 
"""

# this when found a digit, delete from a list the digit and the previous element of the list O(nxm) = O(n^2)
def clearDigits(s: str) -> str:
    s = list(s)
    p1 = 1
    while p1 < len(s) :
        if s[p1].isdigit() :
            del s[p1-1]  
            del s[p1-1]  
            p1 -= 1
            continue
        else :
            p1 += 1
    return "".join(s)

#this algorithm add an element to a new list if it is not a digit else don´t added the element and delete the last 
# element of the list, O(1). So the final complexity is O(n)
def clearDigits_2(s: str) -> str:
    result = []
    for char in s:
        if not char.isdigit() :
            result.append(char)
        else :
            result.pop()
    return "".join(result)

s = "abcde456"
print(clearDigits(s))
print(clearDigits_2(s))