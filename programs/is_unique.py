# implement an algorithm to determinate if a string has all unique characters
# What if cannot use additional structures?

def is_unique(string) -> bool :
    for a in range(0, len(string)-1) :
        for b in range(a+1,len(string)) :
            if string[a] == string[b] :
                return False
    
    return True


string = "abcdefgha"
print(is_unique(string))