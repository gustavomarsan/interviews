
def create_list(n: int) -> list:
    return [i for i in range(n)]

def create_odd_list(n: int) -> list:
    return [i for i in range(n) if i % 2 != 0]
    

n = int(input("Enter the length for the list: "))
print(create_list(n))
print(create_odd_list(n))