"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not 
a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Examplec3:
Input: head = [1,2,3,4,5,6], k = 2
Output: [2,1,4,3,6,5]
Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""
from single_linked_lists import Node

def reverseKGroup(head: Node, k)-> Node:
    if not head or k == 1:
        return head
    new_node = Node(0)
    new_node.next = head
    prev = new_node
    curr = prev.next
    while curr :
        runner = prev
        for i in range(k) :         # check if a reverse loop is possible
            runner = runner.next
            if not runner :           
                return new_node.next
        left_point = prev
        new_right = curr
        for i in range(k) :         # if loop if posible do a loop
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        left_point.next = prev      # make new conections
        new_right.next = curr
        prev = new_right            # prepare prev for next loop, curr is OK
    return new_node.next

a = Node.list_builder()
print(a)
print(reverseKGroup(a, 2))