"""
155. Min Stack
https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

from collections import deque
from heapq import heapify, heappop, heappush

class MinStack:

    def __init__(self):
        self.de = deque([])
        self.minimum = []
        heapify(self.minimum)

    def push(self, val: int) -> None:
        self.de.append(val)
        heappush(self.minimum, val)

    def pop(self) -> None:
        val = self.de.pop()
        self.minimum.remove(val)
        heapify(self.minimum)

    def top(self) -> int:
        return self.de[-1]
        
    def getMin(self) -> int:
        return self.minimum[0]   


my_stack = MinStack()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.getMin())
print(my_stack.top())
my_stack.pop()
my_stack.push(1)
print(my_stack.getMin())
print(my_stack.top())
print(my_stack.de)