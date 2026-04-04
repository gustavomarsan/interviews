"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
# solved with runner tecnique, with two pointers, one pointer will be n nodes ahead of the other pointer, 
# when the first pointer reaches the end of the list, the second pointer will be at the node to be removed, 
# then we can remove it by changing the next pointer of the previous node to point to the next node of the node 
# to be removed.
"""


from single_linked_lists import Node

class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        if not head.next:
            return None 

        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next

        if not p1 :
            return head.next

        while p1.next :
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return head

a = Solution()

head = Node.list_builder()
print(head)

n = int(input("Enter the number of the node to be removed from the end of the list: "))
head = a.removeNthFromEnd(head, n)
print(head)