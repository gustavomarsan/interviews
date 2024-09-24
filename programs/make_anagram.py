"""

A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other
if the first string's letters can be rearranged to form the second string. In other words, both strings must contain 
the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum 
number of character deletions required to make the two strings anagrams. Determine this number.

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions
required to make  a and b anagrams. Any characters can be deleted from either of the strings.

Example
a = "cde"
b = "def"

Delete  e from a and f from b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.

a=fcrxzwscanmligyxyvym
a=accfgilmmnrsvwxxyyyz   ordered

b=jxwtrhvujlmrpdoqbisbwhmgpmeoke
b=bbdeeghhijjklmmmooppqrrstuvwwx    ordered


"""

def makeAnagram(a, b):
    # Write your code here
    a_list = [x for x in a]
    a_list.sort()
    b_list = [x for x in b]
    b_list.sort()
    p = 0                               # p is for pointer
    c = 0                               # c is for count
    while p < len(a_list):              # eliminate elements in a that are not in b
        if a_list[p] not in b_list:
            a_list.pop(p)
            c +=1
            continue
        else :
            p += 1
            continue
    p = 0
    while p < len(b_list):              # eliminate elements in b that are not in a
        if b_list[p] not in a_list:
            b_list.pop(p)
            c +=1
            continue
        else :
            p += 1
            continue
    # now we have the same elements but not the same quantity of chars
    p = 0
    while p < min(len(a_list), len(b_list)):    # compare a and b 1 by one and delete excedent chars
        if a_list[p] != b_list[p]:
            if a_list[p] < b_list[p]:
                a_list.pop(p)
                c += 1
                continue
            else:
                b_list.pop(p)
                c += 1
                continue
        p +=1
    while len(a_list) != len(b_list):           # review the last part of de list when have no the same lenght
        if len(a_list) > len(b_list):
            a_list.pop(-1)
            c +=1
            continue
        if len(b_list) > len(a_list):
            b_list.pop(-1)
            c += 1
            continue
    return c

a = "cde"
b = "abc"

print(makeAnagram(a,b))