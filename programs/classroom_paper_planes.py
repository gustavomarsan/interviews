"""
In a classroom where seats are positioned in a 2D array, students comunicate by throwing paper planes with messages inside them
Some students are acurate when throwing the planes, meaning they won't miss. However, not all of them are equally strong and 
can reach the same distance.
Given a list of the students that can accurately throw planes, a source and a destination, return weather a message could reach
its destination.
(x, y, s)
s is the strenght of the student = radious where it can reach
the paper plane has the source and destination information so it can be re-thrown by another student.
Example:
students = [(0, 0, 5), (4, 1, 4), (4, 4, 3)]
source = 0
destination = 2
output: true
*** Note: check possible neightbors reached by paper plane and reach new neighbors, is student reached is = destination 
we return True, if we finish checking all neighbors and don´t find destination return False. (avoid repeated neighbors)
"""

from collections import deque

def diff(student1: list[int], student2: list[int]) -> bool :
    return (abs(student1[0] - student2[0]) + abs(student1[1] - student2[1])) <= student1[2]     # check if is valid neighbor

def paper_plane(students: list[list[int]], source: int, destination: int) -> bool :
    queue = deque([source])
    visited = {source}
    while queue :
        print(queue, visited)
        student = queue.popleft()
        for i in range(len(students)) :
            if i not in visited and diff(students[student], students[i]) :
                if i == destination :
                    return True
                visited.add(i)
                queue.append(i)
    return False

students = [[0, 0, 5], [2, 2, 5], [1, 4, 6], [4, 1, 4], [5, 2, 6], [6, 6, 3]]
source = 0
destination = 5

print(paper_plane(students, source, destination))