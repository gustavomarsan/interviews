def bubble_sort(a: list) -> list:
    sorted = False
    swaps = 0
    while not sorted:
        sorted = True
        for n in range(len(a)-1):
            if a[n] > a[n+1]:
                sorted = False
                swaps += 1
                a[n], a[n+1] = a[n+1], a[n]

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element:", a[0])
    print("Last Element:", a[-1])
            
    return a


print(bubble_sort([1,4,2,6,5,8,2]))