def urlify(a) -> str :
    b = []
    for n in range(len(a)) :
        if a[n] != " " :
            b.append(a[n])
        else :
            b.append("%20")
    c = "".join(b)
    return c
  
print(urlify(input("Write a string: ")))