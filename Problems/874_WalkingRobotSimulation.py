from typing import *
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def execute(command):
            nonlocal pos
            nonlocal face
            nonlocal farDist
            nonlocal obstacleSet
            if command==-2:
                if face==(0,1):
                    face=(-1,0)
                elif face==(-1,0):
                    face=(0,-1)
                elif face==(0,-1):
                    face=(1,0)
                elif face==(1,0):
                    face=(0,1)
            elif command==-1:
                if face==(0,1):
                    face=(1,0)
                elif face==(1,0):
                    face=(0,-1)
                elif face==(0,-1):
                    face=(-1,0)
                elif face==(-1,0):
                    face=(0,1)
            else:
                while command>0:
                    nextPos=(pos[0]+face[0],pos[1]+face[1])
                    if nextPos in obstacleSet:
                        break
                    pos=nextPos
                    farDist=max(farDist, pos[0]**2+pos[1]**2 )
                    command-=1

        obstacleSet=set()
        for obs in obstacles:
            obstacleSet.add(tuple(obs))
        pos=(0,0)
        face=(0,1)
        farDist=0
        for command in commands:
            execute(command)
        return farDist