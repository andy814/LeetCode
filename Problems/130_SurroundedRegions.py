from typing import *
class Solution:
    def solve(self, board: List[List[str]]) -> None: # we can introduce new variable to record accepted O, which saves space
        """
        Do not return anything, modify board in-place instead.
        """
        zeroSet=set()
        def explore(i,j):
            if board[i][j]=="X":
                return
            zeroSet.add((i,j))
            if i-1>=0 and (i-1,j) not in zeroSet:
                explore(i-1,j)
            if i+1<=len(board)-1 and (i+1,j) not in zeroSet:
                explore(i+1,j)
            if j-1>=0 and (i,j-1) not in zeroSet:
                explore(i,j-1)
            if j+1<=len(board[0])-1 and (i,j+1) not in zeroSet:
                explore(i,j+1)

        for i in range(len(board)):
            explore(i,0)
            explore(i,len(board[0])-1)
        for j in range(len(board[0])):
            explore(0,j)
            explore(len(board)-1,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in zeroSet:
                    board[i][j]="X"