"""""
Given string, find the longest substring without repeated characters ans return the length as int 

longest_substring("abcabcbb") -> 3

"abcaa"

p1 4
p2 5
my_set {a }
max_len 3

"""

def max_substr(a: str)-> int :
    my_set = set()
    p1 = p2 = max_len = 0
    while p2 < len(a) :
        if a[p2] not in my_set :
            my_set.add(a[p2])
            p2 += 1
            max_len = max(max_len, len(my_set))
        else :
            my_set.remove(a[p1])
            p1 +=1
    return max_len

a = "abcdefaghija"
print(max_substr(a))
