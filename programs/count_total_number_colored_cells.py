"""
2579. Count Total Number of Colored Cells
https://leetcode.com/problems/count-total-number-of-colored-cells/
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, 
indicating that you must do the following routine for n minutes:
At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.
Return the number of colored cells at the end of n minutes.
Example 1:
Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:              []
Input: n = 2          [][][]
Output: 5               []
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
Constraints:
1 <= n <= 105
** Note: option 1 biult it whith a loop, seetin an axis of cell large and addind adjacent cell X 2 (2 sides) 
descending quantity. Complexity O(n)

option 2. a Mathematical formula taken from solutions and editorial.  (optimal) O(1)

                     []
                   [][][]
                 [][][][][]
                   [][][]
                     []
"""

def coloredCells(n: int) -> int:
    axis = n * 2  -1
    colored = axis
    axis -= 2
    while axis > 0 :
        colored += 2*axis
        axis -= 2
    return colored

def coloredCells2(n: int) -> int:
    return 2 * n * (n-1) +1

def coloredCells3(n: int) -> int:
    return n**2 + (n-1)**2 



n = 5
print(coloredCells(n))
print(coloredCells2(n))
print(coloredCells3(n))