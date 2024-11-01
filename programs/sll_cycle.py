"""
https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150
141. Linked List Cycle
Easy
Topics
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

"""
from single_linked_lists import Node


a = Node(1)
b = Node(2, a)

def hasCycle(head: Node):
    p1 = head
    p2 = head
    while p2 and p2.next :
        p1 = p1.next 
        p2 = p2.next.next
        if p1 == p2 :
            return True
    return False
        
a = Node(1)
b = Node(2) 
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = b

#print(a)
print(hasCycle(a))
