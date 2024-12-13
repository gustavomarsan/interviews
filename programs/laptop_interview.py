"""
This is a laptop type interview

In memory channel

You will implement a queue in memory for workers to push and get work.
It should read from stdin and write to stdout.

The program must implement the following commands:

ENQUEUE int
Enqueues the integer value into the queue.

PEEK
Checks the next integer value to be poped, without poping it

POP
Gets the next value to work on.

SIZE 
Prints the size of the queue

END
Finish the program

Completeness 50%
Clean 35%
Performance 15%

"""

from collections import deque

class Workers() :
    
    def __init__(self) -> None:
        self.work = deque([]) 
        self.table = {}
        self.backup = None

    def topic(self, topic: str) -> None :
        self.backup = self.work
        if topic not in self.table.keys() :
            self.table[topic] = deque([])
        self.work = self.table[topic]
    
    def unset_topic(self)-> None :
        self.work = self.backup

    def enqueue(self, num: str) -> None:
        self.work.append(num)

    def peek(self) -> int :
        return self.work[0] if len(self.work) > 0 else "QUEUE EMPTY"

    def pop(self) -> int :
        return self.work.popleft() if len(self.work) > 0 else "QUEUE EMPTY"

    def size(self) -> int :
        return len(self.work)
    
    def prienqueue(self, num: str) -> None :
        self.work.appendleft(int(num))

a = Workers()
while True :
    key = input().split()
    if key[0] ==  "ENQUEUE" :
        a.enqueue(key[1])
    if key[0] == "PEEK" :
        print(a.peek())
    if key[0] == "POP" :
        print(a.pop())
    if key[0] == "SIZE" :
        print(a.size())
    if key[0] == "PRIENQUEUE" :
        a.prienqueue(key[1])
    if key[0] == "TOPIC" :
        a.topic(key[1])
    if key[0] == "UNSET_TOPIC" :
        a.unset_topic()
    if key[0] == "END" :
        break

