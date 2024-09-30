""""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing 
bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, 
{[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, 
unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:
*It contains no unmatched brackets.
*The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given a string of brackets, determine if is balanced. If a string is balanced, return YES. Otherwise, return NO.

{[()]}          True
{[(])}          False
{{[[(())]]}}    True
"""

from collections import deque

def isBalanced(s):
    if len(s) % 2 == 1:
        return False
    a = deque([])
    my_dict = {")": "(", "]" : "[", "}" : "{"}
    for item in s:
        if item == "[" or item == "(" or item == "{":
            a.append(item)
            continue
        if len(a) == 0:
            return False
        x = a.pop()
        if my_dict[item] != x:
            return False
    return len(a) == 0 
            
    

s = "[{"
print(isBalanced(s))

