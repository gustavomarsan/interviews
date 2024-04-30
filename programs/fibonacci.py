def fibonacci(a: int) -> list:
    fibo = [0, 1]
    limit = 0
    while a > limit:
        limit = fibo[-1] + fibo[-2]
        fibo.append(limit)

    return fibo


print(fibonacci(int(input("Fibonacci up to number: "))))
