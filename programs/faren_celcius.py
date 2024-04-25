def celcius(far: int) -> int:
    cel = (far - 32) * (5 / 9)
    return cel


print("Celcius", celcius(int(input("Farenheit: "))))
