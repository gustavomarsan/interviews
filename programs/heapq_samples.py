from heapq import heapify, heappop, heappush

numbers = [2, 4, 21, 5 ,9, 2, 7, 8]

print(numbers)

heapify(numbers)

print(numbers)

heappush(numbers, 1)
print(numbers)

x = heappop(numbers)
print(x)
print(numbers)