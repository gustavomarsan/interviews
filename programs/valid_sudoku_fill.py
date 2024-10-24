"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

[["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]


backtracking:
"""

def backtracking(board, i, j, row, col, square) -> bool:
    if j > 8 :
        j = 0
        i += 1
    if i > 8 :
        return True

    if board[i][j] != "." :
        return backtracking(board, i, j+1, row, col, square)
    for n in range(1, 10) :
        if str(n) not in row[i] and str(n) not in col[j] and str(n) not in square[i // 3][j // 3] :
            #print(i, j, row[i], col[j], n)
            board[i][j] = str(n) 
            row[i].add(str(n))
            col[j].add(str(n))
            square[i // 3][j // 3].add(str(n))
            if backtracking(board, i, j+1, row, col, square) :
                return True
            row[i].remove(str(n))
            col[j].remove(str(n))
            square[i // 3][j // 3].remove(str(n))
            board[i][j] = "."

    return False
                
    
def fill_sudoku(board:list[list[int]]) -> None :
    row = [set() for x in range(9)]
    col = [set() for x in range(9)]
    square = [[set() for x in range(3)] for y in range(3)]
    
    for i in range(9) :
    	for j in range(9) :
            if board[i][j] == "." : 
                continue
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            square[i // 3][j // 3].add(board[i][j])
    backtracking(board, 0, 0, row, col, square)


board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

for i in range(9) :
    print(board[i])
print("---------------------------------------------")
fill_sudoku(board)
for i in range(9) :
    print(board[i])