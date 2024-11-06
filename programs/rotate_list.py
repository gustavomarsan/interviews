"""

"""
from single_linked_lists import Node

def rotate_list(head: Node, k) :
    if not head or k == 0 or head.next == None :
        return head
    len_head = 1

    # calculate len of linked list
    count = head
    while count.next :
        len_head += 1
        count = count.next
    if k >= len_head :      # if k > len_head
        k = k % len_head
    p1 = head
    p2 = head 
    for i in range(k) :  # to runner (p2) walks k steps
        if p2.next :         # if k > len onthe linkedt list then begin again
            p2 = p2.next
        else :
            p2 = head
    
    if p2 == head :          # if loop ends in head node 
        return head
    
    while p2.next  :            # find the last element from p2 and walks both pointer 
        p1 = p1.next
        p2 = p2.next

    new_head = p1.next 
    p2.next = head
    p1.next = None
    return new_head

head = Node.list_builder()
print(head)
print(rotate_list(head, 2))