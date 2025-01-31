"""
1462. Course Schedule IV
https://leetcode.com/problems/course-schedule-iv/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, 
then course a is a prerequisite of course c.
You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
Return a boolean array answer, where answer[j] is the answer to the jth query.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
Example 4:
numCourses = 5
prerequisites = [[4,3],[4,1],[4,0],[3,2],[3,1],[3,0],[2,1],[2,0],[1,0]]
queries = [[1,4],[4,2],[0,1],[4,0],[0,2],[1,3],[0,1]]
Constraints:
2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= numCourses - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 104
0 <= ui, vi <= numCourses - 1
ui != vi
***Note: I guess i could be solve by 2 walks in pre_req. once left to right, once right to left
** but in longer list of pre_req (more than 50) need to walk 4 times instead 2 (I dont know why).
"""

from operator import itemgetter

def checkIfPrerequisite(numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    n = len(queries)
    answer = [False] * n
    pre_req = {}       # dict. key = course, value {pres, pres}
    prerequisites.sort(key=itemgetter(1))
    for req, course in prerequisites :
        if course not in pre_req :
            pre_req[course] = {req}
        else :
            pre_req[course].add(req)
        if req in pre_req :
            pre_req[course].update(pre_req[req])
    
    print(pre_req)    
    prerequisites.sort(key=itemgetter(1), reverse=True)
    for req, course in prerequisites :
        if course not in pre_req :
            pre_req[course] = {req}
        else :
            pre_req[course].add(req)
        if req in pre_req :
            pre_req[course].update(pre_req[req])
    
    print(pre_req)  
    """
    prerequisites.sort(key=itemgetter(1))
    for req, course in prerequisites :
        if course not in pre_req :
            pre_req[course] = {req}
        else :
            pre_req[course].add(req)
        if req in pre_req :
            pre_req[course].update(pre_req[req])

    print(pre_req)        
    prerequisites.sort(key=itemgetter(1), reverse=True)
    for req, course in prerequisites :
        if course not in pre_req :
            pre_req[course] = {req}
        else :
            pre_req[course].add(req)
        if req in pre_req :
            pre_req[course].update(pre_req[req])
    print(pre_req)
    """
    for i in range(n) :
        pre = queries[i][0]
        course = queries[i][1]
        if course in pre_req and pre in pre_req[course] :
            answer[i] = True
    return answer

numCourses = 5
prerequisites = [[4,3],[4,1],[4,0],[3,2],[3,1],[3,0],[2,1],[2,0],[1,0]]
queries = [[1,4],[4,2],[0,1],[4,0],[0,2],[1,3],[0,1]]
print(checkIfPrerequisite(numCourses, prerequisites, queries))