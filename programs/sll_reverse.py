"""
Reverse a linked list
example
input
a -> b -> c ->  null
output
c-> b-> a-> None
"""

from single_linked_lists import Node

def reverse_linked_list(a: Node)-> Node :  
    prev = None
    curr = a
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

a = Node.list_builder()
print(a)
print(reverse_linked_list(a))
