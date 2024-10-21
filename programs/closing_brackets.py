"""""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Input: s = "()[]{}"

Output: true

Input: s = "(]"

Output: false

Input s = ")"

"""

def is_balanced(s: str)-> bool :
    stack = []
    pairs = { ")": "(", "]": "[", "}": "{"}
    for char in s :
        if char in ("[", "{", "(") :
            stack.append(char)
            continue
        if len(stack) == 0 :
            return False
        if pairs[char] != stack.pop() : 
            return False
    return len(stack) == 0

s = "(([{{[[{[{[]}]}]]}}]))"
print(is_balanced(s))