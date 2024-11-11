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
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""
from single_linked_lists import Node

def reverseBetween(head: Node,  left: int, right: int) -> list[int] :
    new_head = Node(0)          # add a previuse element to head   0 -> head
    new_head.next = head  
    prev = new_head
    curr = head
    for i in range(right ) :  # walk to reach right
        next = curr.next
        if i == left -1 :
            left_point = prev       # is the node before the switch will start
            left_node =  curr       # is the node where thje switch will start
        if i > left -1 :
            curr.next = prev        # reverse order in nodes betwen left and right
        prev = curr
        curr = next
    left_point.next = prev          # connect with de right node to switch
    left_node.next = next           # connect with the nodes behind the right node
    return new_head.next         

a = Node.list_builder()
print(a)
print(reverseBetween(a, 2, 2))


