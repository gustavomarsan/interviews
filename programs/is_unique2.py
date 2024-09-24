
def is_unique(string)  -> bool :
    for p1 in range(len(string)-1) :
        for p2 in range(p1+1, len(string)) :
            if string[p1] == string[p2] :
                return False
    
    return True


print(is_unique(input("wirte a string: ")))