"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

"""

def isPalindrome(s: str)-> bool :
    new_s = [char for char in s.lower() if char.isalnum()]
    print(s.lower())
    print(new_s)
    for i in range(len(new_s) // 2) :
        if new_s[i] != new_s[~i] :
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))