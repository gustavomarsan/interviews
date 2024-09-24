# given a list of numbers, return a list of the posicion on the numbers in value order from top to bottom
# example:   [9, 5, 4, 1, 6, 8, 8]  return [1, 4, 5, 6, 3, 2, 2]
# top ordered values are 9:1, 8:2, 6:3, 5:4, 4:5, 1:6

def places(numbers: list) -> list :
    numbers_ordered = []
    for item in numbers :
        numbers_ordered.append(item)
    numbers_ordered.sort(reverse=True)
    
    table = {}
    place = 0
    for item in numbers_ordered :
        if item not in table :
            place +=1
            table[item] = place
    for n in range(len(numbers)) :
        numbers_ordered[n] = table[numbers[n]]

    return numbers_ordered


a = [9, 5, 4, 1, 6, 8, 8, 2, 2]
print(a)
print(places(a))

