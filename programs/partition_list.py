"""
0 -> 1  -> 1 -> 
     prev  curr next
    less
"""
from single_linked_lists import Node
def partition(head, x):
    new_head = Node(0)              # insert a node before the head
    new_head.next = head
    less = new_head                 # node with value < x to know where to insert in case need to move
    prev = head  
    curr = head.next
    if prev.data < x :
        less = prev
    while curr :
        next = curr.next
        if curr.data < x and prev != less:      # swith values
            curr.next = less.next
            less.next = curr
            less = curr
            prev.next = next
            curr = next
            continue
        if curr.data  < x :         # update less
            less = curr
        prev = curr
        curr = next
    return new_head.next

a = Node.list_builder()
print(a)
print(partition(a, 5))
        
