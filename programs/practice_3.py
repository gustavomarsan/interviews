"""
This is an example for enclosure.
Each time we call make_multiplier with a different n, it creates a new multiplier function that 
retains access to the value of n that was passed to make_multiplier at the time of its creation.
This allows us to create multiple multiplier functions with different behaviors based on the value of n.
"""



def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50


