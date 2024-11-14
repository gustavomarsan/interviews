"""
https://leetcode.com/problems/merge-k-sorted-lists/description/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:
Input: lists = []
Output: []
Example 3:
Input: lists = [[]]
Output: []
Note : use heaps adding the firs node of each element of the list

"""
from heapq import heapify, heappop, heappush
from single_linked_lists import Node
def mergeKLists(lists: list[Node])-> Node:
    my_list = [(node.data,i) for i, node in enumerate(lists) if node]
    heapify(my_list)
    new_ll  = Node(0)
    prev = new_ll
    while my_list :
        _, index = heappop(my_list)
        prev.next = lists[index]
        prev = prev.next
        lists[index] = lists[index].next
        if lists[index] : 
            heappush(my_list, (lists[index].data, index))
            
    return new_ll.next

a = Node.list_builder()
b = Node.list_builder()
c = Node.list_builder()
d = Node.list_builder()
            
print(a)
print(b)
print(c) 
print(d)
lists = [a, b, c, d]
print(mergeKLists(lists))