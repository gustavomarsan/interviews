# iterator example
class CountUpTo:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Example of Class CountUpTo by using a generator function
def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

# generator function example (uses yield)
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


numbers = [x for x in range(1,10)]
print("numbers type:", type(numbers))  # Output: <class 'list'>

# Generator expression example
result = (num for num in numbers if num % 2 == 0)

print("result type", type(result)) # Output: <class 'generator'>

for even_number in result:
    print("number", even_number)  # Output: 2, 4, 6"""

print(list(result)) # Output: [] because once then generator is used, it is exhausted

ev_num = even_numbers(numbers)
print(type(ev_num))  # Output: <class 'generator'>
print(ev_num)  # Output: <generator object even_numbers at 0x...>
print(list(ev_num))  # Output: 2, 4, 6, 8

my_generator = even_numbers(numbers)

for even_number in my_generator:
    print(even_number)

print(list(my_generator))  # Output: [] because once then generator is used, it is exhausted

s = "hello"
letters = (letter for letter in s)
print(type(letters))  # Output: <class 'generator'>
print(list(letters))  # Output: h, e, l, l, o
print(type(letters))  # Output: <class 'generator'>
print(list(letters))  # Output: [] because once then generator is used, it is exhausted


#lambda function example
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))      # filter is a filter object
print(even_numbers)     # Output: 2, 4, 6, 8   type list
print(even_numbers)     # Output: 2, 4, 6, 8   type list is not exhausted because it is a list, not a generator
