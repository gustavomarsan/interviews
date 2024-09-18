import math 

def find_numbers(array) :

    dict = { }


    for item in array :
        if item in dict :
            dict[item] += 1
        else :
            dict[item] = 1

    print(dict.items())


    for i in range(len(array)-1) :
        a = array[i]
        for j in range (i+1, len(array)) :
            b = array[j]
            if a == b :
                continue                                # it isn´t possible that a and b could be the same value 
            c = math.sqrt( a**2 + b**2 )
            if c in dict or -c in dict:                 # c could be positive or negative to match the trinomial
                if c in dict :                          # determinate if c is positive or negative
                    key = c
                else :                                  # and moved to key
                    key = -c
                if dict[key] > 1 :                      # if yes,  no problem that  c = a or c = b
                    return a, b, int(key)
                elif c == a or c == b :                 # if c = a or c = b and there are only one c, it doesn´t match
                    continue
                else :                                  # match is valid, a b and c are different, no probleam how many values have
                    return a, b, int(key)     
           
    return None, None                                   # No values found


array = [4, 12, 8, -5, 6, -3] 

print(find_numbers(array))