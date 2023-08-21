# Given 2 strings check if s2 is a rotation of s1 using one call


def string_rotation(s1, s2):
    if s1 == s2:
        return True

    # put the strings in lists to work in lists not in strings
    l1 = []
    for i in s1:
        l1.append(i)
    l2 = []
    for i in s2:
        l2.append(i)

    for i in range(len(l2) - 1):
        l2.append(l2[0])
        l2.pop(0)
        if l2 == l1:
            return True

    # if the program never match
    return False

    # if s1 == s2 :
    #    return True


print(string_rotation(input(), input()))
