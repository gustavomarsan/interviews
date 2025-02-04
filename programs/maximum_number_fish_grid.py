"""
2658. Maximum Number of Fish in a Grid
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:
Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
Example 1:
Input: grid = 
[[0,2,1,0]
,[4,0,0,3]
,[1,0,0,4]
,[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:
Input: grid = 
[[1,0,0,0]
,[0,0,0,0]
,[0,0,0,0]
,[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
****Note: Solved by BFS checking neighbors in a queue
"""

def findMaxFish(grid: list[list[int]]) -> int:
    def check_neighbors(row: int, col: int)-> None :    #add neighbors to a  queue
        if row > 0 and grid[row-1][col] > 0 and (row-1, col) not in visited :
            neighbors.append((row-1, col))
        if row +1 < len(grid) and grid[row+1][col] > 0 and (row+1, col) not in visited :
            neighbors.append((row+1, col))
        if col > 0 and grid[row][col-1] > 0 and (row, col-1) not in visited :
            neighbors.append((row, col-1))
        if col +1 < len(grid[0]) and grid[row][col+1] > 0 and (row, col+1) not in visited :
            neighbors.append((row, col+1))

    visited = set()
    neighbors = ([])
    maximum = 0
    for row in range(len(grid)) :
        for col in range(len(grid[0])) :
            if grid[row][col] == 0 or (row, col) in visited:
                continue
            neighbors = ([])
            count = grid[row][col]
            visited.add((row, col))
            check_neighbors(row, col)
            while len(neighbors) > 0 :
                r, c = neighbors.pop()
                count += grid[r][c]
                visited.add((r, c))
                check_neighbors(r, c)
                
            maximum = max(maximum, count)
    return maximum

grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
print(findMaxFish(grid))
