"""
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) 
as long as you use only a stack's standard operations.


"""

class MyQueue:

    def __init__(self):
        self.a = []        
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)
        return
        
    def pop(self) -> int:
        if self.empty():
            return
        
        if len(self.b) == 0:
            self.flush()
        
        return self.b.pop()
        

    def peek(self) -> int:
        if self.empty():
            return
        if len(self.b) > 0:
            return self.b[-1]
        else:
            return self.a[0]

    def empty(self) -> bool:
        return len(self.a) == 0 and len(self.b) == 0

    def flush(self) -> None:
        while len(self.a) > 0:
            self.b.append(self.a.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
            
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.empty())
obj.push(5)
obj.push(6)


