def string_rotation(s1, s2):
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


print(string_rotation(input(), input()))
