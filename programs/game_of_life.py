"""
https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the 
British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or 
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following 
four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

[0, 1, 0]     [0, 0, 0]
[O, O, 1] --> [1, 0, 1]
[0, 0, 0]     [0, 1, 0]

"""

def gameOfLife(board: list[list[int]]):
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            # get lives from neighbors
            n_lives = 0
            if i -1 >= 0 and j - 1 >= 0 and abs(board[i-1][j-1]) == 1 :
                n_lives += 1
            if i -1 >= 0 and abs(board[i-1][j]) ==1 :
                n_lives += 1
            if i -1 >= 0 and j + 1 < len(board[0]) and abs(board[i-1][j+1]) ==1 :
                n_lives += 1
            if j -1 >= 0 and abs(board[i][j-1]) == 1 :
                n_lives += 1
            if j +1 < len(board[0]) and abs(board[i][j+1] == 1) :
                n_lives += 1
            if i +1 < len(board) and j -1 >= 0 and abs(board[i+1][j-1]) == 1 :
                n_lives += 1
            if i +1 < len(board) and abs(board[i+1][j]) == 1 :
                n_lives +=1
            if i +1 < len(board) and j +1 < len(board[0]) and abs(board[i+1][j+1]) == 1 :
                n_lives += 1
            # action         -2 is for previus and now is a 1.      -1 is for a prevuis 1 and now is 0
            if board[i][j] == 0 and n_lives == 3 :
                board[i][j] = -2
            if board[i][j] == 1 and n_lives in (0, 1, 4, 5, 6 , 7, 8) :
                board[i][j] = -1
        # replace       -2 -> 1  and   -1 -> 0
    for i in range(len(board)) :
        board[i][:] = [1 if x == -2 else 0 if x == -1 else x for x in board[i]]        #substituing with list comprenhension
    return board

a = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
for item in a:
    print(item)
print("------------")
board = gameOfLife(a)
for item in board:
    print(item)
