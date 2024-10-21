# calcular el factorial de un numero


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    elif n > 1:
        return n * factorial(n - 1)

    return -1


print("Su factorial es:", factorial(int(input("Dame un numero: "))))
