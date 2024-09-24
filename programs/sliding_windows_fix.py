# given a string and a lenght (k) find the maximum substring and return the sum of the k elements and de index
# fix sliding window algorithm

def max_substr(a: list, k :int) -> int:
    max = 0
    index = 0
    for n in range(k) :
        max += a[n]
    new_ac  = max
    for n in range(k, len(a)) :
        new_ac = new_ac -a[n-k] + a[n]
        if new_ac > max :
            max  = new_ac
            index = n-k+1
    return max, index

    
a = [10, 2, 5, 6, 9, 23, 1, 34, 5, 13, 1, 39 , 4]

print(a)
print("r:", max_substr(a, 4))


