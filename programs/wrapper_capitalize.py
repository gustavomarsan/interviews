from functools import wraps

def capital(func):
    def wrapper(*args, **kwargs):
        first = args[0].capitalize()
        last = args[1].capitalize()
        result = func(*(first, last), **kwargs)
        return result
    return wrapper

@capital
def get_name(first_name: str, last_name: str)-> str:
    return first_name, last_name
  
  
print(get_name("pablo", "gomez"))

