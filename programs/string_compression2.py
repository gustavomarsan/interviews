def str_compress(string) :
    dict = {}
    for item in range(len(string)) :
        if string[item] in dict :
            dict[string[item]] += 1
        else :
            dict[string[item]] = 1
    
    if len(dict) * 2 >= len(string) : 
        return string
    new_string = ""
    for item in dict :
        new_string = new_string + item + str(dict[item])

    return new_string

print(str_compress(input("Write a string of chars: ")))
