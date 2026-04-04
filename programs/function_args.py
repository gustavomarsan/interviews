def sum_of_nums(a: int, b: int, *args, name: str, level: str)-> int: 
    sum_of_all = a + b
    if args:
        sum_of_all += sum(args)

    if level == "High":
        print("This information is clasified")

    return f"{name} the sum of your nums is: {sum_of_all}"




print(sum_of_nums(5, 7, name="Juan", level = "Mid"))