def reverse_string(x):
    return x[::-1]


a = "Hello World"

b = reverse_string(a)

print(a)
print(b)

print(a[::-1])  # print reversed list
print(b[::-1])  # print reversed list


fruits = ["orange", "apple", "pear"]
print(fruits)
print(fruits[::-1])  # print reversed list
fruits.append("grape")  # insert element at the end of the list
print(fruits)
fruits.reverse()  # reverse the list
print(fruits)
fruits.append("lime")
print(fruits)
print(list(reversed(fruits)))  # return list reversed
print(fruits)
fruits.insert(0, "melon")  # insert an element ina position required
print(fruits)
fruits.insert(1, "papaya")  # insert an element ina position required
print(fruits)
fruits.insert(-1, "mango")  # insert an element ina position required
print(fruits)
print(fruits[::-1])
fruits.pop(0)
print(fruits)
