"""
Given a chess board, and two postions (x1, y1 - x2, y2) , return the number of hops a knight would have to make to go from 
position 1 to position 2 (x1, y1 = knight, x2, y2 = target )

"""
from collections import deque

def chess_board_print(a: list[list]) -> None:
    print("------------------------")
    for n in range(len(a)):
        print(a[n])
def knigh_hops(x1, y1, x2, y2) -> int:
    board = [[0 for _ in range(8)] for _ in range(8)]
    board[y1][x1] = "K"
    board[y2][x2] = "T"
    chess_board_print(board)
    queu = deque([(x1, y1)])
    board[y1][x1] = 1
    while queu:
        x, y = queu.popleft()
        for col in range(+2, -3, -1):               # this 2 loops create the 8 posible neighbors
            for row in range(+2, -3, -1) :
                if (row + y) > 7 or (col + x) > 7 or (row + y) < 0 or (col + x) < 0:
                    continue                        # quit if pointer is out of range
                if abs(row) == abs(col)  :
                    continue                        # quit, we need a L movement
                if row == 0 or col == 0 :
                    continue                        # quit, we need a L movement
                if board[row+y][col+x] == "T" :     # found
                    chess_board_print(board)
                    return board[y][x]
                if board[row+y][col+x] == 0 :       # this position hasn't checked and add to queu
                    board[row+y][col+x] = board[y][x]+1
                    queu.append((x+col, y+row))

print("movs =", knigh_hops(3,5,1,2))    # x, y order, knight and target

