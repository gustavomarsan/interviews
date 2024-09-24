# write a methodto replace all spaces  in a string with "%20" 
# be careful with the spaces at the end

def urlify (string) -> str :
    list = []
    for x in range (len(string)-1, -1, -1) :        # It reads in reverse order to avoid spaces in the final 
        if string[x] == " " :
            if len(list) == 0 :                     # if the final is a space do not substitute
                continue
            list.append("%20")
            continue
        list.append(string[x])
    list.reverse()
    result = "".join(list)   
    return result


string = "Mr. John Smith method        "
print(urlify(string))