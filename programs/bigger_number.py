def bigger_number(a: int, b: int) -> int:
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Are equals"


a = 14
b = 14

print(bigger_number(a, b))
