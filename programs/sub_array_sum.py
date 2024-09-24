# Given an array and a target t, determine how many subarrays add up to the target t
# using sliding window with poinyers p1 an p2 in complexito O(n)

def is_sub_array(a: list, t: int)-> int :
    p1 = p2 = 0
    c = 0 
    sum = a[0]
    while p1 < len(a) and p2 < len(a) :
        if sum < t :
            p2 +=1
            if p2 < len(a) :
                sum  += a[p2]
        if sum > t :
            sum -= a[p1]
            p1 += 1
        if sum == t :
            c += 1
            sum -= a[p1]
            p1 += 1
    return c

arr = [ 5, 2, 3, 2, 1, 2, 3]

print(is_sub_array(arr, 3))

