"""
Implement a heap

The parent is at index (i-1)/2 (using integer division). 
The left child is at index 2*i + 1. The right child is at index 2*i + 2.

r  1
  
   6
  / \
 4   3
/ 
5  

new_value = 0
parent =  0

Note : implement in a list, tou using a heapq
"""

class Heap :
    def __init__(self) -> None:
        self.heap = []

    def parent(self, index: int) -> int :
        return (index -1) // 2

    def left(self, index: int) -> int :
        return 2 * index +1
    
    def right(self, index: int) -> int :
        return 2 * index +2
    
    def swap(self, x: int, y: int) -> None :
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def push(self, value: int) -> None :
        i = len(self.heap)
        self.heap.append(value)
        parent = self.parent(i)
        while i > 0 and self.heap[i] < self.heap[parent] :
            self.swap(i, parent)
            i = parent
            parent = self.parent(i)

    def peak(self) -> int :
        return self.heap[0]
    
    def pop(self) -> int :
        if len(self.heap) == 0:
            return None
        ans = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0
        left = self.left(i) 
        right = self.right(i)
        while left < len(self.heap) :               # if there is not left, there is not right
            if right < len(self.heap) and self.heap[right] < self.heap[left] and self.heap[right] < self.heap[i] :
                self.swap(right, i)
                i = right
            elif self.heap[left] < self.heap[i] :
                self.swap(left, i)
                i = left
            else :                                  # if left and right are grater than i then exit
                break
            left = self.left(i) 
            right = self.right(i)

        return ans

a = Heap()
a.push(4)
a.push(1)
a.push(2)
print(a.heap)
a.push(8)
print(a.heap)
print(a.pop())
print(a.pop())
print(a.heap)
a.push(5)
a.push(3)
print(a.heap)
print(a.peak())
