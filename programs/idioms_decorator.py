from datetime import datetime
import time
from functools import wraps



def example_wrapper(func):
    def wrapper(*args, **kwargs):
        # tasks before running the function
        result = func(*args, **kwargs)
        # tasks after running the function
        return result
    return wrapper



def launching_message(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        for i in range(5, 0, -1):
            print(f"Launching function {func.__name__} in {i} seconds...")
            time.sleep(1)
        result = func(*args, **kargs)
        return result
    return wrapper
        


def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()        # Start time measurement
        print(f"Start execution time {datetime.fromtimestamp(start_time):%Y-%m-%d %H:%M:%S}")
        result = func(*args, **kwargs)  # exectute the function that call decorator
        end_time = time.time()          # End time measurement
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result                   # Return the result of the original function
    return wrapper

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result to be returned: {result}")
        return result
    return wrapper


# this functions returns sum a and b and spend time simulating execution time
@launching_message
@time_counter
@log_call
def sum_and_spending_time(n: int, a:int, b:int)-> int:
    time.sleep(n)       # simulate execution time
    return (f"The sum of {a} and {b} is {a + b}")


a = 5
b = 3
time_seconds = 5
print(sum_and_spending_time(time_seconds, a, b))




