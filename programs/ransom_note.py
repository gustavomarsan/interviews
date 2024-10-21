"""""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica 
of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly 
using whole words from the magazine; otherwise, print No.

Uppercase and lower case count.

 magazine = "attack at dawn", note = "Attack at dawn",  -> No
"""

def checkMagazine(magazine, note):
    # Write your code here
    dict_m = {}
    for item in magazine:
        dict_m[item] = dict_m.get(item, 0 ) +1
    for x in note:
        if x not in dict_m or dict_m[x] == 0:
            return "No"
        dict_m[x] -=1
        
    return "Yes"



a= "two times three is not four"

b = "two times not"

print(checkMagazine(a, b))        