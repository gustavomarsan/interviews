from heapq import heapify, heappop, heappush

a = [8, 9, 23, 26, 2, 4, 7]

heapify(a)
print(a)

heappush(a, 1)

print(a)

x  = heappop(a)

#heappop(a)

print(x)
print(a)
print(a[0])