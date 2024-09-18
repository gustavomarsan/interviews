# gioven two strings, write a method  to decide if one string is a permutation of the other.

def is_permutation(a,b) -> bool :

    if len(a) != len(b) :           # if the string are different lengh is False
        return False
    str_a = []
    str_b = []
    for x in range (len(a)) :       # copy values of each strinf to a list
        str_a.append(a[x])
        str_b.append(b[x])
    str_a.sort()                    # index the lists to compare element by element
    str_b.sort()
    for x in range (len(str_a)) :   # if all of the elements are equal then it is True
        if str_a != str_b :
            return False
    return True


a="dearing"
b="reading"
print(is_permutation(a,b))