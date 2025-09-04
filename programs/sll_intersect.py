"""""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

given 2 sll determinate if they have an intersection, if yes return de Node if not return None

example 1:
a -> b -> c -> d -> e                   a, b, c, d, e
        /
h -> g                                  h, g, c, d, e

retur Node c

example 2:
a -> b -> c -> d -> e                   a, b, c, d, e

h -> g -> l -> m -> n                   h, g, l, m, n

return None

"""
from single_linked_lists import Node

def lenght(a: Node) -> int:
    l = 0
    while a:
        l += 1
        a = a.next
    return l

def intersect(a: Node, b: Node) -> Node :
    la = lenght(a)
    lb = lenght(b)

    if lb > la :
        a, b = b, a
        
    for n in range(abs(la - lb)) :
        a = a.next

    while a :
        if a == b :
            return a 
        a = a.next
        b = b.next
    
    return None

a = Node("a")
a.next = Node("b")
a.next.next = Node("c")
a.next.next.next = Node("d")
a.next.next.next.next = Node("e")

b = Node("h")
b.next = Node("g")
b.next.next = a.next.next   # existent Node(c)

print(intersect(a, b))


