"""
Paint fully a chess board (8X8) only to practice a BFS since a initial point, painting the continuos places
"""
from collections import deque

def chess_board_print(a: list[list]) -> None:
    print("------------------------")
    for n in range(len(a)):
        print(a[n])
def paint(x, y) -> int:
    a =[[0 for _ in range(8)] for _ in range(8)]
    a[y][x] = 1
    chess_board_print(a)
    queue = deque([(x, y)])
    while queue :
        x, y = queue.popleft()
        for col, row in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1),  (-1, 1), (-1, 0), (-1, -1)]:
            if 0 <= x+col <= 7 and 0 <= y+row <= 7 and a[y+row][x+col] == 0:
                queue.append((x+col, y+row))
                a[y+row][x+col] = 1
    chess_board_print(a)



paint(0, 0)    # x, y order

