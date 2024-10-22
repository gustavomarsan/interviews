# Create a class deque, with function peek, pop, put

from collections import deque

class MyQueue:
    def __init__(self):
        self.value = deque([])
    
    def peek(self):
        return self.value[0]
        
    def pop(self):
        self.value.popleft()
        
    def put(self, value):
        self.value.append(value)



a = MyQueue()
print(type(a))
a.put(1)
a.put(2)
a.put(3)
a.put(5)
a.put(7)
print(a.value)
print(a.peek())
x = a.pop()
print(x)
print(a.value)
a.put(80)
a.put(12)
a.put(9)
print(a.value)
for _ in range(3) :
    a.pop()

print(a.value)