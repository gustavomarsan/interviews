def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        y = 3
        return x + y
    
    print("inside", x)
    return inner()
print(outer())

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

funcs = []
for i in range(3):
    def f():
        print(i)
    funcs.append(f)

for f in funcs:
    f()

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(9))  
print(double(2))

