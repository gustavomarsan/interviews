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

    for i in range(len(l2) - 1):  # rotate l1 char by char
        temp = l2[0]
        for n in range(len(l2) - 1):  # rotate l1 char by char
            l2[n] = l2[n + 1]
        l2[-1] = temp
        if l2 == l1:
            return True

    # if the program never match
    return False

    # if s1 == s2 :
    #    return True


print(string_rotation(input(), input()))
