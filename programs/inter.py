"""
Given a string s consisting of small English letters, find and return the first instance of a character that repeats N times. If there is no such character, return '_' underscore - dash

s = "ssddfftthhshawwll" -> s

s = "ssddfftthhhawwlls" -> h

dict {"s": 2, "d": 2, "f": 2, "t": 2, "h": 3}


time O(n)
space O(n)

"""

def repeated(s:str, n:int ) -> str :
    table = {}
    for item in s :
        if item in table :
            table[item] += 1
            if table[item] == n :
                return item
        else :
           table[item] = 1
    return "-"

"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'

s = "abcab" => c
s = "abcabc" => _

dict = {"a": 2, "b": 2, "c": 1}

s = "abcabd" => c

dict = {"a": 2, "b": 2, "c":1, "d": 1 }


"""

def non_repeated(s:str) -> str :
    table = dict()
    for item in s :
        if item in table :
            table[item] += 1
        else :
            table[item] = 1
    # fill the dict 
 
    for item in table.items() :
        if item[1] == 1 :
            return item[0]
    return "_"

a = "abcabdd"
print(non_repeated(a))
print(repeated(a,3))