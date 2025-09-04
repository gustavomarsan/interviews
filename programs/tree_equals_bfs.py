"""
https://leetcode.com/problems/same-tree/
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

This solution is by iteretively
"""
from binary_tree_base import Node
from collections import deque
    
def equals(p, q) -> bool :
        deque_p = deque([])
        deque_q = deque([])
        deque_p.append(p)
        deque_q.append(q)
        while deque_p and deque_q:
            p_n = deque_p.popleft()
            q_n = deque_q.popleft()
            if p_n is None and q_n is None:
                continue
            if p_n is None or q_n is None:
                return False
            if p_n.data == q_n.data:
                deque_p.append(p_n.left)
                deque_p.append(p_n.right)
                deque_q.append(q_n.left)
                deque_q.append(q_n.right)
            else:
                return False
            
        return True  

            
            
tree_a = Node(None)
Node.insert(80, tree_a)
Node.insert(150, tree_a)
Node.insert(145, tree_a)
Node.insert(20, tree_a)
Node.insert(40, tree_a)
Node.insert(10, tree_a)
Node.insert(45, tree_a)
Node.insert(50, tree_a)
Node.insert(5, tree_a)
Node.insert(35, tree_a)
Node.insert(55, tree_a)
Node.insert(160, tree_a)
Node.insert(170, tree_a)
Node.insert(180, tree_a)
Node.insert(140, tree_a)
Node.insert(135, tree_a)

tree_b = Node(None)
Node.insert(80, tree_b)
Node.insert(150, tree_b)
Node.insert(145, tree_b)
Node.insert(20, tree_b)
Node.insert(40, tree_b)
Node.insert(10, tree_b)
Node.insert(45, tree_b)
Node.insert(50, tree_b)
Node.insert(5, tree_b)
Node.insert(35, tree_b)
Node.insert(55, tree_b)
Node.insert(160, tree_b)
Node.insert(170, tree_b)
Node.insert(180, tree_b)
Node.insert(140, tree_b)
Node.insert(135, tree_b)

a = [tree_a]
visited_nodes = []
#Node.bfs_print(tree_a, visited_nodes, a)

a = [tree_b]
visited_nodes = []
#Node.bfs_print(tree_b, visited_nodes, a)

print(equals(tree_a, tree_b))
    