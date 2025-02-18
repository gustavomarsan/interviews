from heapq import heapify, heappop, heappush

# a = [8, 9, 23, 26, 2, 4, 7]

# a = [("0012", 0), ("1131", 1), ("0600", 2), ("1000", 0) ]

a = [["0012", 0, True, ], ["1131", 1, True],["0600", 2, False], ["1000", 0, False] ]

heapify(a)
print(a)

heappush(a, ["0931", 5, False])

print(a)

time, worker, job_done = heappop(a)

#heappop(a)

print(job_done)
print(a)
print(a[0])

if a[0][0] < "1000" :
    print("yes")
    time, worker, job_done  = heappop(a)
    print(worker)