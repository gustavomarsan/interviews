"""
https://leetcode.com/problems/word-search/description/
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
Input: board =  [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:
Input: board =  [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
Input: board =  [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCB"
Output: false
"""

def find_char(board: list[list[str]], word: str, word_index: int, x: int, y: int, my_set: set ) -> bool :
  	# stop
    if word_index == len(word) :
        return True
    
    # recursion 
    if (x, y -1) not in my_set and y - 1 >= 0 and word[word_index] == board[x][y- 1] :
        my_set.add((x, y-1))
        if find_char(board, word, word_index +1, x , y -1, my_set) :
            return True
        my_set.remove((x, y -1))
    if (x -1, y) not in my_set and x - 1 >= 0 and word[word_index] == board[x-1][y] :
        my_set.add((x -1, y))
        if find_char(board, word, word_index +1, x-1 , y, my_set) :
            return True
        my_set.remove((x -1, y))
    if  (x +1, y) not in my_set and x + 1 < len(board) and word[word_index] == board[x +1][y] :
        my_set.add((x +1, y))
        if find_char(board, word, word_index +1, x+1 , y, my_set):
            return True
        my_set.remove((x +1, y))
    if (x, y+ 1) not in my_set and y + 1 < len(board[0]) and word[word_index] == board[x][y +1] :
        my_set.add((x, y + 1))
        if find_char(board, word, word_index+ 1, x , y+1, my_set) :
            return True
        my_set.remove((x, y +1))
    return 
  

def find_word(board: list[list[str]], word: str) -> bool :
    my_set = set()
    for x in range(len(board)) :
        for y in range(len(board[0])) :
            if board[x][y] == word[0] :
                my_set.add((x, y))
                if find_char(board, word, 1, x,y, my_set) :
                    return True
                my_set.remove((x, y))
                
    return False
board = [["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]]
word =  "AAB"
print(find_word(board, word))