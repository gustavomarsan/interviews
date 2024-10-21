"""
Given to strings s1 and s2, return if within s1 there is a permutation of s2

"abcdehg" "ba" -> true

"abcdehg" "ac" -> false

SOLVED with dict, s2 subtract elements in the dict subs1 add elements in the dict- when dict is empy s2 and subs1 are ==
"""

def substr_permutation(s1: str, s2: str)-> bool :
    my_dict = {}
    for i in s2 :               # adding s2 in negative numbers
        my_dict[i] = my_dict.get(i, 0) - 1 
    for i in range(len(s2)) :   # add the first subs1 with positive numbers. Create the sliding window
        my_dict[s1[i]] = my_dict.get(s1[i], 0) + 1 
        if my_dict[s1[i]] == 0 :
                my_dict.pop(s1[i])
    if len(my_dict) == 0 :      # if dict is empty then measn that in s2 is in subs1 and return True
        return True
    p1 = 0
    p2 = p1 + len(s2)
    # move the sliding window with pointers p1 __ p2
    while p2 < len(s1) :            
        # get out p1
        my_dict[s1[p1]] = my_dict.get(s1[p1], 0) - 1
        if my_dict[s1[p1]] == 0 :
            my_dict.pop(s1[p1])

        #get in p2
        my_dict[s1[p2]] = my_dict.get(s1[p2], 0) + 1 
        if my_dict[s1[p2]] ==0 :
            my_dict.pop(s1[p2])
        
        if len(my_dict) == 0 :      # if dict is empty then measn that in s2 is in subs1 and return True
            return True
        p1 += 1
        p2 += 1
    return False

s1 = "kbcderf"
s2 = "dcb"
print(substr_permutation(s1, s2))

