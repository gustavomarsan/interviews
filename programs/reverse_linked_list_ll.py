"""
https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the 
list from position left to position right, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
                 l   r
Output: [1,4,3,2,5]
Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
Note : check if left is in the begining of the list and if left is in the last element

"""
from single_linked_lists import Node
def reverseBetween(head: Node,  left: int, right: int) -> list[int] :
    if left == right :          # there no reverse
        return head
    p1 = head
    if left > 1 :               # to find the previous an the first node to reverse
        for _ in range(left - 2) :
            p1 = p1.next
        left_point = p1         # left point is the previous node to reverse linked list
        new_right = p1.next     # new right is the first node in the reverse that becames right
    else :                      # if reverse node begin in first node
        new_right = head
        left_point = Node(0) 
    previous = new_right
    current = new_right.next
    for _ in range(right - left) : # swap nodes pointers from 1st to last 
        if current.next :
            next_node = current.next
        else :
            next_node = None        # if linked list is finished next:node will be None
        current.next = previous
        previous = current
        if current.next :
            current = next_node
    left_point.next = previous      # previous node to the reverse point to las in reverse
    new_right.next = next_node      # new right point to the next element if there isn´t then none 
    return head if left > 1 else left_point.next        # else is for reverse start in first element


a = Node.list_builder()
print(reverseBetween(a, 3, 5))


