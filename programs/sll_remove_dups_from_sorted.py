"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
82. Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Input: head = [1,1,1,2,3]
Output: [2,3]

"""
from single_linked_lists import Node

def deleteDuplicates(head: Node)-> Node :
    if head == None or head.next == None:
        return head
    dups = set()
    p1 = head.next
    prev = head.data
    while p1 :      # read all the list and store dups in a set
        if p1.data == prev:
            dups.add(p1.data)
        prev = p1.data
        p1 = p1.next
    while head.data in dups :    # check if head is not in dups until head is non repeated
        head = head.next
        if head == None :       # if all the list haa repeated numbers return None
            return None
    # skip dups
    p1 = head
    p2 = head.next
    while p2 :
        if p2.data not in dups :
            p1.next = p2
            p1 = p1.next
        else :
            p1.next = None
        p2 = p2.next
    return head
        

print(deleteDuplicates(Node.list_builder()))

