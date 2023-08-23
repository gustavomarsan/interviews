# implement a method to perform a basic string compression using the counts of repetead characters
# if the compressed string would not become smaller, the method should return the original string
# do not be concatenating strings repeatly


def stringCompression(a):
    last_char = a[0]
    cont = 0
    b = []
    for i in range(len(a)):
        new_char = a[i]
        if new_char == last_char:
            cont += 1
        else:  # add info to list when char changes
            b.append(last_char)
            b.append(str(cont))
            last_char = new_char
            cont = 1

    # add the last info
    b.append(last_char)
    b.append(str(cont))

    bstring = "".join(b)

    if len(bstring) < len(a):
        return bstring
    else:
        return a


print(stringCompression(input()))
