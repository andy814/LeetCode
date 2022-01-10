import collections
from typing import *
import cProfile
import sys

class SolutionQ1:
    def checkString(self, s: str) -> bool:
        ret=True
        encounterB=False
        for char in s:
            if char=="b":
                encounterB=True
            if encounterB==True and char=="a":
                ret=False
                break
        return ret

class SolutionQ2:
    def numberOfBeams(self, bank: List[str]) -> int:
        factors=[]
        for row in bank:
            num1=self.count1(row)
            if num1!=0:
                factors.append(num1)
        if len(factors)<2:
            return 0
        count=0
        for i in range(len(factors)-1):
            count+=factors[i]*factors[i+1]
        return count

    def count1(self,row:str)->int:
        count=0
        for element in row:
            if element=="1":
                count+=1
        return count

class SolutionQ3:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        ret=True
        sortedArr=sorted(asteroids)
        for i in range(len(sortedArr)):
            mass=self.collide(mass,sortedArr[i])
            if mass==-1:
                ret=False
                break
        return ret

    def collide(self,mass,asteroid):
        if mass>=asteroid:
            mass+=asteroid
        else:
            mass=-1
        return mass

class SolutionQ4:
    def maximumInvitations(self, favorite: List[int]) -> int:
        E={}
        for i in range(len(favorite)):
            E[i]=favorite[i]
        VCs=[]
        for i in range(len(favorite)):
            VCs.append(self.calMinVC(i,E))
        print("VCs:",VCs)
        VCs.sort()
        
        return VCs[-1]
    '''
    def calMinVC(self,src,E):
        visited=[src]
        curr=src
        count=0
        while E[curr] not in visited:
            curr=E[curr]
            visited.append(curr)
            count+=1
        if count==2:
            count=max(2,len(visited))
        if len(E)>=2:
            return max(count,2)
        else:
            return len(E)
    '''
    def calMinVC(self,src,E):
        visited=[src]
        curr=src
        while E[curr] not in visited:
            curr=E[curr]
            visited.append(curr)
        count=0
        start=E[curr]
        end=curr
        while start!=end:
            #print("start:",start)
            count+=1
            start=E[start]
        count+=1
        if count==2:
            count=max(2,len(visited))
        #print("returning:",count)
        return count
#[1,0,0,2,1,4,7,8,9,6,7,10,8]
#expected 6,output 5

'''
class CorrectSolutionQ4: #backup
    def maximumInvitations(self, favorite: List[int]) -> int:
        
        visited=[-1]*len(favorite) # -1 unvisited, 0 processing, 1 visited
        graph=collections.defaultdict(list)
        for i in range(len(favorite)):
            graph[i].append(favorite[i])
        maxCircleLen=0
        for i in range(len(favorite)):
            if visited[i]==-1:
                depth=[float("inf")]*len(visited)
                depth[i]=0
                visited[i]=0
                maxCircleLen=max(self.DFS(i,visited,graph,depth,maxCircleLen),maxCircleLen)
        
        mutualPairs=[]
        visited=[-1]*len(favorite)
        for i in range(len(favorite)): # find all the mutual favorite pairs
            if i==favorite[favorite[i]] and visited[i]==-1 and visited[favorite[i]]==-1:
                mutualPairs.append((i,favorite[i])) 
                visited[i]=1
                visited[favorite[i]]=1

        revGraph=collections.defaultdict(list)
        for i in range(len(favorite)):
            revGraph[favorite[i]].append(i)

        count=0
        for a,b in mutualPairs:
            aLen=self.calcDepth(a,revGraph,b)
            bLen=self.calcDepth(b,revGraph,a)
            count+=aLen+bLen

        return max(count,maxCircleLen)
    
    def DFS(self,src,visited,graph,depth,maxCircleLen):
        for adjV in graph[src]:
            if visited[adjV]==-1:
                visited[adjV]=0
                depth[adjV]=depth[src]+1
                maxCircleLen=max(self.DFS(adjV,visited,graph,depth,maxCircleLen),maxCircleLen)
            elif visited[adjV]==0: #processing
                maxCircleLen=max(maxCircleLen,depth[src]-depth[adjV]+1)
            else: #visited
                pass
        visited[src]=1
        return maxCircleLen

    def calcDepth(self,src,revGraph,exclude=None):
        depth=0
        for child in revGraph[src]:
            if child!=exclude:
                depth=max(depth,self.calcDepth(child,revGraph))
        return depth+1
'''

class CorrectSolutionQ4: 

    def maximumInvitations(self, favorite: List[int]) -> int:    
        visited=[-1]*len(favorite) # -1 unvisited, 0 processing, 1 visited
        graph=favorite
        maxCircleLen=0
        for i in range(len(favorite)):
            if visited[i]==-1:
                visited[i]=0
                maxCircleLen=max(self.DFS(i,visited,graph,maxCircleLen),maxCircleLen)
        
        mutualPairs=[]
        visited=[-1]*len(favorite)
        for i in range(len(favorite)): # find all the mutual favorite pairs
            if i==favorite[favorite[i]] and visited[i]==-1 and visited[favorite[i]]==-1:
                mutualPairs.append((i,favorite[i])) 
                visited[i]=1
                visited[favorite[i]]=1

        revGraph=collections.defaultdict(list)
        for i in range(len(favorite)):
            revGraph[favorite[i]].append(i)

        count=0
        for a,b in mutualPairs:
            aLen=self.calcDepth(a,revGraph,b)
            bLen=self.calcDepth(b,revGraph,a)
            count+=aLen+bLen

        return max(count,maxCircleLen)
    
    def DFS(self,src,visited,graph,maxCircleLen):
        adjV=graph[src]
        if visited[adjV]==-1:
            visited[adjV]=0
            maxCircleLen=max(self.DFS(adjV,visited,graph,maxCircleLen),maxCircleLen)
        elif visited[adjV]==0: #processing
            maxCircleLen=max(maxCircleLen,self.calcCycle(adjV,src,graph))
        else: #visited
            pass
        visited[src]=1
        return maxCircleLen

    def calcDepth(self,src,revGraph,exclude=None):
        depth=0
        for child in revGraph[src]:
            if child!=exclude:
                depth=max(depth,self.calcDepth(child,revGraph))
        return depth+1

    def calcCycle(self,src,dst,favorite):
        count=1
        while src!=dst:
            count+=1
            src=favorite[src]
        return count

class IntegratedSolutionQ4:
    def maximumInvitations(self, favorite: List[int]) -> int:
        A=favorite
        n, maxc = len(A), 0
        seen = [0] * n
        for idx in range(n):
            if seen[idx] == 0:
                start=idx
                cur_people=idx
                curset = set()
                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = A[cur_people]
                if cur_people in curset:
                    cursum=len(curset)
                    while start != cur_people:
                        cursum -= 1
                        start = A[start]
                    maxc = max(maxc, cursum)
        maxCircleLen=maxc
        mutualPairs=[]
        visited=[-1]*len(favorite)
        for i in range(len(favorite)): # find all the mutual favorite pairs
            if i==favorite[favorite[i]] and visited[i]==-1 and visited[favorite[i]]==-1:
                mutualPairs.append((i,favorite[i])) 
                visited[i]=1
                visited[favorite[i]]=1

        revGraph=collections.defaultdict(list)
        for i in range(len(favorite)):
            revGraph[favorite[i]].append(i)

        count=0
        for a,b in mutualPairs:
            aLen=self.calcDepth(a,revGraph,b)
            bLen=self.calcDepth(b,revGraph,a)
            count+=aLen+bLen

        return max(count,maxCircleLen)
    
    def DFS(self,src,visited,graph,depth,maxCircleLen):
        for adjV in graph[src]:
            if visited[adjV]==-1:
                visited[adjV]=0
                depth[adjV]=depth[src]+1
                maxCircleLen=max(self.DFS(adjV,visited,graph,depth,maxCircleLen),maxCircleLen)
            elif visited[adjV]==0: #processing
                maxCircleLen=max(maxCircleLen,depth[src]-depth[adjV]+1)
            else: #visited
                pass
        visited[src]=1
        return maxCircleLen

    def calcDepth(self,src,revGraph,exclude=None):
        depth=0
        for child in revGraph[src]:
            if child!=exclude:
                depth=max(depth,self.calcDepth(child,revGraph))
        return depth+1

sys.setrecursionlimit(100000)

#sol=IntegratedSolutionQ4()
#print(sol.maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8]))


mysol=CorrectSolutionQ4()
#cProfile.run("mysol.maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8])")

print(mysol.maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8]))



