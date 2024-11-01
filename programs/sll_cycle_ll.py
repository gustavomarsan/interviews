"""
https://leetcode.com/problems/linked-list-cycle-ii/

0 -> 1 -> 2 -> 3 -> 4

          s
                    f     
"""
from single_linked_lists import Node

def detectCycle(head:Node)-> Node:
    if not head :
        return None
    slow = head
    fast = head
    while head :
        if not fast.next or not fast.next.next :   # there is not a cycle
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            slow2 = head
            while True :
                if slow2 == slow :
                    return slow
                slow = slow.next
                slow2 = slow2.next
                    

a = Node(1)
b = Node(2) 
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = b

print(detectCycle(a).data)



