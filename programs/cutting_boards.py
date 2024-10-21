""""
Alice gives Bob a board composed of  1 x 1 wooden squares and asks him to find the minimum cost of breaking the board back down 
into its individual squares. To break the board down, Bob must make cuts along its horizontal and vertical lines.

To reduce the board to squares, Bob makes horizontal and vertical cuts across the entire board. Each cut has a given cost,
or for each cut along a row or column across one board, so the cost of a cut must be multiplied by the number of segments 
it crosses. The cost of cutting the whole board down into  squares is the sum of the costs of each successive cut.

example

6 4  (dimentions)
we will receive a cost_y and cost_x lists than indicated the cost of each cut and how many cuts we need

cost_y = [2 1 3 1 4]
cost_x = [4 1 2]

"""
from heapq import heapify, heappop

def boardCutting(cost_y: list, cost_x: list)-> int:
    # Write your code here
    for n in range(len(cost_y)) :
        cost_y[n] *= -1
    for n in range(len(cost_x)) :
        cost_x[n] *= -1
    cost = 0
    cut_y = 0
    cut_x = 0
    heapify(cost_y)
    heapify(cost_x)
    while cost_y and cost_x:
        if cost_y[0]*-1 > cost_x[0]*-1  or (cost_y[0] == cost_x[0] and cut_x < cut_y):
            c = -heappop(cost_y)
            cost += c + c * cut_x
            cut_y += 1
            continue
        else:
            c = -heappop(cost_x)
            cost += c + c * cut_y
            cut_x += 1
            continue
    while cost_y or cost_x:
        if cost_y and not cost_x:
            c = -heappop(cost_y)
            cost += c + c * cut_x
            cut_y += 1
        if not cost_y and cost_x:
            c = -heappop(cost_x)
            cost += c + c * cut_y
            cut_x += 1
    return cost
            
        

cost_y = [41, 22, 12, 46, 29, 63, 43, 42, 17, 26, 90, 52, 72, 44, 69, 77, 31, 13, 5, 10, 86, 8, 78, 50, 9, 71, 89, 11, 60, 42, 77, 1, 16, 90, 48, 45, 5, 43, 88, 22, 69, 30, 26, 42, 74, 48, 71, 57, 13, 28, 67, 51, 89, 97]
cost_x = [2, 50, 69, 91, 61, 81, 86, 91, 83, 2, 81, 31, 48, 86, 26, 88, 60, 96, 70, 38, 90, 44, 38, 13, 53, 51, 93, 73, 3, 82, 22, 57, 32, 91, 48, 46, 25, 34, 37, 8, 37, 70, 91, 37, 8, 17, 25, 68, 65, 95, 58, 55, 91, 97, 20, 96, 0, 14, 69, 3, 48, 92, 60, 81, 35, 61, 79]

#cost_y = [1, 1, 2, 3, 4]
#cost_x = [1, 2, 4]

print(boardCutting(cost_y, cost_x))
