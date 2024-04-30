def move_zeroes(a):
    left = 0
    right = 0
    while right < len(a):
        while a[right] == 0 and right < len(a):
            right += 1

            if right == len(a):
                break

        if right == len(a):
            break

        temp = a[left]
        a[left] = a[right]
        a[right] = temp

        left += 1
        right += 1

    return a


a = [1, 2, 9, 0, 2, 1]
print(a)
a = move_zeroes(a)
print(a)
