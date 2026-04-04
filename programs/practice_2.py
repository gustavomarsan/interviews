"""
Implement a function that reverses an input string, but this function
should only reverse alphabetic characters

input_str[a.bcd] =  rever = [a, b].  = [d.cb]
"""
 


def special_reverse(input_str: str) -> str:
    list_2 = []
    new_input = []
    for s in input_str:
        if s.isalpha():
            list_2.append(s)
        new_input.append(s)

    for i in range(len(input_str)):
        if new_input[i].isalpha():
            new_input[i] = list_2.pop()

    return "".join(new_input)


def count_chars(insput_str: str):
    count_dict = {}
    for char in insput_str:
        count_dict[char] = count_dict.get(char, 0) + 1

    return count_dict

assert special_reverse("abcd") == "dcba"
assert special_reverse("a.bcd") == "d.cba"
assert special_reverse("#ab.c%d") == "#dc.b%a"
assert special_reverse("#$$&") == "#$$&"

result = count_chars("asdfggfseessz")
for key, value in result.items():
    print(f"{value} times --> {key}")