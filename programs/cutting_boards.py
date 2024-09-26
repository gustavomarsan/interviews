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

def boardCutting(cost_y: list, cost_x: list)-> int:
    # Write your code here
    cost = 0
    cut_y = 0
    cut_x = 0
    cost_y.sort()
    cost_x.sort()
    while cost_y and cost_x:
        if cost_y[-1] > cost_x[-1] or (cost_y[-1] == cost_x[-1] and cut_x < cut_y):
            c = cost_y.pop()
            cost += c + c * cut_x
            cut_y += 1
            continue
        else:
            c = cost_x.pop()
            cost += c + c * cut_y
            cut_x += 1
            continue
    while cost_y or cost_x:
        if cost_y and not cost_x:
            c = cost_y.pop()
            cost += c + c * cut_x
            cut_y += 1
        if not cost_y and cost_x:
            c = cost_x.pop()
            cost += c + c * cut_y
            cut_x += 1
    return cost
            
        

#cost_y = [71, 58, 61, 51, 33, 3, 43, 48, 94, 30, 29, 40, 59, 83, 12, 43, 64, 69, 64, 65, 42, 57, 40, 72, 64, 98, 98, 47, 56, 6, 85, 79, 65, 46, 30, 98, 49, 25, 98, 96, 7, 27, 88, 66, 10, 0, 62, 26, 69, 78, 92, 64, 87, 84, 88, 51, 35]
#cost_x = [87, 50, 91, 45, 35, 22, 62, 81, 53, 61, 83, 30, 59, 31, 38, 39, 19, 56, 1, 20, 70, 28, 41, 48, 72, 57, 35, 56, 46, 39, 91, 85, 41, 34, 30, 77, 57, 93, 10]
cost_y = [1,1,2,3,4] 
cost_x = [1,2,4]

print(boardCutting(cost_y, cost_x))