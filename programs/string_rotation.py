# chech if one stirng is a rotation from other string

def string_rotation(s1, s2) -> bool :       # this function will compare char by char changing the pointer to initialize
    # if s1 and s1 are equal, s2 is not an rotation of s1
    if s1 == s2:
        return False

    # if s1 and s2 have not the same len, then s2 is not a rotatiion of s1
    if len(s1) != len(s2):
        return False

    # loop j is to initialize pointer in s2 in diferent place every cycle
    for j in range(len(s2)):
        equal = True
        # loop  i  is to walk pointers
        for i in range(len(s1)):
            # walk p1 and p2 1 by 1 to compare and begining in diferent points every for i
            if s1[i] != s2[((i + j) % len(s1))]:
                equal = False
                break
        # if loop i was completed it means the complete cycle was equal s1 and s2
        if equal:
            return True

    # if the program never match
    return False

def str_rotation(s1, s2) -> bool :      # this function will find fi is a rotation by concatening s1+s1
                                        # if s2 is in (s1+s1) then it bis true
    x = s1+s1
    s3 = "".join(x)
    search = s3.find(s2)
    if search ==  -1 :
        return False
    return True



s1=input()
s2=input()
print(string_rotation(s1, s2))
print(str_rotation(s1, s2))