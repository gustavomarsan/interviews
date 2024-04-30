def farenheit(cel: int) -> int:
    far = (cel * (9 / 5)) + 32
    return far


print("Farenheit", farenheit(int(input("Celcius: "))))
