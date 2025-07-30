"""
https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
Input: board = 

[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

"""
def isValidSudoku2(board: list[list[str]]) -> bool:     # solution from leetcode
    cols = [set() for _ in range(9)]
    squares = [[set() for _ in range(3)] for _ in range(3)]

    for x in range(9):
        rows = set()
        for y in range(9):
            value = board[x][y]
            if value == ".":
                continue
            if value in rows or value in cols[y] or value in squares[x//3][y//3]:
                return False

            rows.add(value)
            cols[y].add(value)
            squares[x//3][y//3].add(value)
        
        return True

def isValidSudoku(board):           # my solution
    my_sety = [set() for n in range(9)]
    for x in range(len(board)) :    # check in lines and colums 
        my_setx = set()    
        for y in range(len(board)) :
            if board[x][y] == "." :
                continue
            if board[x][y] in my_setx or board[x][y] in my_sety[y]:
                return False
            my_setx.add(board[x][y])
            my_sety[y].add(board[x][y])
    
    for x in (0, 3, 6) :            #check in squares
        for y in (0, 3, 6) :
            my_set = set()
            for i in range(3) :
                for j in range(3) :
                    if board[x+i][y+j] == "." :
                        continue
                    if board[x+i][y+j] in my_set :
                        return False
                    my_set.add(board[x+i][y+j])
    
    return True


a = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku2(a))
print(isValidSudoku(a))