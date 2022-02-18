from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(ent,word,trace):
            
            startX=ent[0]
            startY=ent[1]
            if len(word)==1:
                if board[startY][startX]==word:
                    return True
                else:
                    return False

            flag1=flag2=flag3=flag4=False

            if startX>0 and board[startY][startX-1]==word[1] and (startX-1,startY) not in trace:
                trace.append((startX-1,startY))
                flag1=dfs((startX-1,startY),word[1:],trace)
                trace.pop()

            if startX<len(board[0])-1 and board[startY][startX+1]==word[1] and (startX+1,startY) not in trace:
                trace.append((startX+1,startY))
                flag2=dfs((startX+1,startY),word[1:],trace)
                trace.pop()

            if startY>0 and board[startY-1][startX]==word[1] and (startX,startY-1) not in trace:
                trace.append((startX,startY-1))
                flag3=dfs((startX,startY-1),word[1:],trace)
                trace.pop()

            if startY<len(board)-1 and board[startY+1][startX]==word[1] and (startX,startY+1) not in trace:
                trace.append((startX,startY+1))
                flag4=dfs((startX,startY+1),word[1:],trace)
                trace.pop()

            if flag1 or flag2 or flag3 or flag4:
                return True
            else:
                return False
            
        entry=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    entry.append((j,i))

        for ent in entry:
            if dfs(ent,word,[ent]) == True:
                return True

        return False