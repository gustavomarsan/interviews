"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = 0->[1,2,3,4]

Output: [2,1,4,3]

Example 2
Input: head = [1,2,3]

Output: [2,1,3]
	         p  
             c
"""
from single_linked_lists import Node

def swap_pairs(root: Node)-> Node :
    new_head = Node(0)
    new_head.next = root
    prev = new_head
    curr = new_head.next
    while curr and curr.next :
        # swap
        next = curr.next
        curr.next = next.next
        prev.next = next
        next.next = curr
        # prepare next
        prev = curr
        curr = prev.next
    return new_head.next

a = Node.list_builder()
print(a)
print(swap_pairs(a))