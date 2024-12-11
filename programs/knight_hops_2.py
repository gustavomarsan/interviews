"""
Given a chess board, and two postions (x1, y1 - x2, y2) , return the number of hops a knight would have to make to go from 
position 1 to position 2  (x1, y1 = knight, x2, y2 = target )

comments:  the knight_hops_2 it is ok for BFS becuase it satisfies the rule of:
while
first eliminate the next data in the queue
then check if this data is that we need for the operation and 
then add the childs to de queue (recursion)
end loop 
"""
from collections import deque

def chess_board_print(a: list[list]) -> None:
    print("------------------------")
    for n in range(len(a)):
        print(a[n])
def knigh_hops(x1, y1, x2, y2) -> int:
    board = [[0 for _ in range(8)] for _ in range(8)]
    queue = deque([(x1, y1)])
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2 :
            chess_board_print(board)    
            return board[y][x]
        for col, row in [(2, 1), (2, -1), (1, 2), (1, -2), (-1, +2), (-1, -2), (-2, +1), (-2, -1)]:
            if 0 <= x + col <=7 and 0 <= y+row <= 7 and board[row+y][col+x] == 0 :
                board[row+y][col+x] = board[y][x]+1
                queue.append((x+col, y+row))
        chess_board_print(board)

print("movs =", knigh_hops(3,5,1,2))    # x, y order, knight and target

