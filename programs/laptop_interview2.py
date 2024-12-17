"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 

key value type store
key - value

If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Explanation
LRUCache lRUCache = new LRUCache(2);       
x <- head  <-> N(1) <-> N(3)
{1 : (1, N(1)), 3 : (3, N(3)), }
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

put(100, 10) ?
capacity= 0
table = {1: 1, 2:_2}

output = 1

LRUCache lRUCache = new LRUCache(3);      
lRUCache.put(1, 1); // cache is {1=1}				([1])
lRUCache.put(2, 2); // cache is {1=1, 2=2}			([2, 1])
lRUCache.put(3, 3); // cache is {1=1, 2=2, 3=3}		([3, 2, 1])
lRUCache.get(1);    // return 1						([1, 3, 2])
lRUCache.get(3);    // return 3						([3, 1, 2])
lRUCache.put(4, 4); // cache is {1=1, 4=4, 3=3}		([4, 3, 1])

O(1)
k {v, Nodo}

https://leetcode.com/problems/lru-cache/
https://www.geeksforgeeks.org/lru-cache-implementation/

"""
class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return str(self.val) + " -> " + str(self.next) 


class Queue:
    # Queue is double linked list to set the LRU in order and access them in O(1) 
    # Queue nodes =   head -> LRU node -> node -> node -> ...  lastNode -> None

    def put(head: Node, a: Node, last: Node) -> None :      
        if head.next :
            b = head.next       # b is previous LRU, a is new LRU
            b.prev = a
        else :
            last = a 
        a.next = head.next
        head.next = a
        a.prev = head
        return last
    
    def update(head: Node, a: Node, last: Node) -> None :
        if a.prev != head :
            if a == last :
                last  = a.prev              #update last
            #conect previous neighbors
            a.prev.next = a.next            # connect prev to next
            if a.next :                  
                a.next.prev = a.prev        # connect next to prev
            # conect a to head
            a.next = head.next
            a.prev = head
            a.next.prev = a
            head.next  = a
        return last

    def trunc_queue(last: Node) -> None :   # update last, eliminate last and prev became last
        new_last = last.prev
        new_last.next = None
        last.prev = None
        return new_last

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity            
        self.table = {}                     # dict key: (val, Node)         (node for LRU queue)
        self.head = Node(0)                 # is for queue of LRU
        self.last = None                    # is for set last Node in queue to trunc queue in case it gets full capacity

    def get(self, key: int) -> int :
        if key in self.table.keys() :
            self.last = Queue.update(self.head, self.table[key][1], self.last)      # update queue
            print("QUEUE", self.head, "LAST", self.last.val)
            return self.table[key][0]
        return -1
    
    def put(self, key: int, value: int) -> None :
        if key in self.table.keys() :
            self.table[key][0] = value
            self.last = Queue.update(self.head, self.table[key][1], self.last)      # update queue
            print("QUEUE", self.head, "LAST", self.last.val)
            return
        a = Node(key)
        self.table[key] = [value, a]
        self.last =  Queue.put(self.head, a, self.last)         # update queue
        if len(self.table) > self.capacity :                    # update queue length
            self.table.pop(self.last.val)                       # delete last from dict
            self.last = Queue.trunc_queue(self.last)            # update queue
        print("QUEUE", self.head.next, "LAST", self.last.val)
        return

a = LRUCache(3)
while True :
    inkey = input().split()
    if inkey[0] == "GET" :
        print(a.get(inkey[1]))
    if inkey[0] == "PUT" :
        a.put(inkey[1], inkey[2])
    if inkey[0] == "END" :
        break
