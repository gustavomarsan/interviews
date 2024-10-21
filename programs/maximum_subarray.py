# Given a list of numbers, find the maximum sum of a contiguous subarray.
#
# Kadane's algorithm


def max_subarray(a):
    max_sum = a[0]
    current_sum = a[0]
    ini = 0
    fin = 0
    for i in range(1, len(a)):
        if a[i] > (a[i] + current_sum):
            current_sum = a[i]
            ini = i
        else:
            current_sum += a[i]
        if current_sum > max_sum:
            max_sum = current_sum
            fin = i
    return max_sum, ini, fin

a = [9, -4, 6, 7, -20, 50, 2, 10, 3, -50]

print(a)
print("The maximun sub-array is: ", max_subarray(a))
