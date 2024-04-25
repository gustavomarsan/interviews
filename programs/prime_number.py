def is_prime(a: int) -> bool:
    for x in range(2, a):
        if a % x == 0:
            return False
    return True


print(is_prime(int(input("Is prime number: "))))
