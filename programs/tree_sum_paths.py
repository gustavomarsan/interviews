"""
Given a binary tree and an integer target, return all the paths that add up to the target number.
From the root to the leaf


"""

from binary_search_tree import Node

def check_sum(a: Node, target, sum)-> int :
    if a == None :
        return 0
    
    if a.left == None and a.right == None and a.data + sum == target :
        return 1 

    return check_sum(a.left, target, sum+ a.data) + check_sum(a.right, target, sum+ a.data)


def sum_paths(a: Node, target) -> int :
    return check_sum(a, target, 0)


a = Node(1)
a.left = Node(1)
a.right = Node(2)
a.left.left = Node(1)
a.left.right = Node(2)
a.left.right.left = Node(-1)


print(sum_paths(a, 3))