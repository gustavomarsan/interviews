# Given 2 strings check if s2 is a rotation of s1 using one call, supouse the 2 strings are the same large


def string_rotation(s1, s2):
    if s1 == s2:
        return True

    # put the strings in lists to work in lists not in strings
    l1 = []
    l2 = []
    for i in range(len(s1)):
        l1.append(s1[i])
        l2.append(s2[i])

    for i in range(len(l2) - 1):
        l2.append(
            l2[0]
        )  # rotate l2 in 2 setps, copy [0] at the end and delete it from de begining
        l2.pop(0)
        if l2 == l1:  # compare rotated l2 with l1
            return True

    # if the program never match
    return False


print(string_rotation(input(), input()))

#    l1 = []
#    for i in s1:
#        l1.append(i)
#    l2 = []
#    for i in s2:
#        l2.append(i)
