# Given a list of numbers, find the maximum sum of a contiguous subarray.


def max_subarray(a):
    max_sum = a[0]
    current_sum = a[0]
    ini = 0
    fin = 0

    for i in range(1, len(a)):
        if a[i] > (a[i] + current_sum):
            current_sum = a[i]
            print("---", a[i])
            ini = i

        else:
            current_sum += a[i]
            print("add", a[i], current_sum)

        if current_sum > max_sum:
            max_sum = current_sum
            print("new max", max_sum)
            fin = i

    return max_sum, ini, fin


a = [1, 4, 5, 7, -2, -5, 2, -10, -3, 5]

print(a)
print("The maximun sub-array is: ", max_subarray(a))
