
from collections import deque

word = { "Brand" : "ford", "Year": 2022, "Type" : "Sport"}

myset = {"1", "2", "4", "3", "5", "6"}

a = deque(["a", "b", "c"])

x = ["x", "y", "z"]

a.append("d")
a.extend(x)
a.extend(x)
a.extend("b")
a.extendleft("b")
a.extendleft(word)
#a.extend(myset)

print(a)
a.pop()
a.insert(3, "Hola")
print(a)
print(a.count("b"))
a.remove("b")
print(a)


""""
deque.remove(element)   remove the first element from left to right. Only one element
deque.count(element)    return the number that element 
deque.insert(index, element)    insert an element in the index given

"""
