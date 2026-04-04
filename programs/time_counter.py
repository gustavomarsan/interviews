from datetime import datetime
import time
from functools import wraps

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
