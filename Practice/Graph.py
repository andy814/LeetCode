from collections import deque

class Graph: #
    def __init__(self,V=None,E=None):
        self.V=V
        self.E=E
    
    def BFS(self,src):
        visited=[False]*len(self.V)
        queue=deque()
        queue.append(src)
        while queue:
            currV=queue.popleft()
            if visited[currV]==False:
                print(currV,"->",end=" ")
                visited[currV]=True
                adjV=self.E[currV]
                for v in adjV:
                    queue.append(v)
        print("")
    
    def DFS(self,src,visited=None):
        if visited==None:
            visited=[False]*len(self.V)
        #print("visited:",visited)
        stack=deque()
        stack.append(src)
        while stack:
            currV=stack.pop()
            if visited[currV]==False:
                print(currV,"->",end=" ")
                visited[currV]=True
                adjV=self.E[currV]
                for v in adjV:
                    self.DFS(v,visited)

    def standardDFS(self,src):
        visited=[]
        stack=deque()
        stack.append(src)
        while stack:
            currV=stack.pop()
            if currV not in visited:
                visited.append(currV)
                for V in self.E[currV]:
                    if V not in visited:
                        stack.append(V)
        return visited

    def standardBFS(self,src):
        visited=[]
        queue=deque()
        queue.append(src)
        while queue:
            currV=queue.popleft()
            if currV not in visited:
                visited.append(currV)
                for V in self.E[currV]:
                    if V not in visited:
                        queue.append(V)
        return visited       

    def quickBFS(self,src): # note that we changed the position of visited check
        visited=[src]
        queue=deque()
        queue.append(src)
        while queue:
            currV=queue.popleft()
            for V in self.E[currV]:
                if V not in visited:
                    visited.append(V)
                    queue.append(V)
        return visited         

    def standardRecursiveDFS(self,src,visited=None):
        if not visited:
            visited=[]
        visited.append(src)
        for V in self.E[src]:
            if V not in visited:
                self.standardRecursiveDFS(V,visited)
        return visited

    def calcDegree(self):
        count=dict((u,0) for u in self.V)
        for v in self.V:
            for adjv in self.E[v]:
                count[adjv]+=1
        return count

    def topologySort(self,directed=True):
        degree=self.calcDegree()
        result=[]
        if directed:
            while 0 in degree.values():
                for v in degree.copy():
                    if degree[v]==0:
                        degree.pop(v)
                        result.append(v)
                        for adjv in self.E[v]:
                            degree[adjv]-=1
        else:
            while 1 in degree.values():
                for v in degree.copy():
                    if degree[v]==1:
                        degree.pop(v)
                        result.append(v)
                        for adjv in self.E[v]:
                            degree[adjv]-=1

        if len(result) != len(self.V):
            return None
        else:
            return result

    def standardTopologySort(self,directed=True):
        degree=self.calcDegree()
        seq=[]
        if directed:
            Q=deque([u for u in degree if degree[u]==0])
            while Q:
                curr=Q.popleft()
                seq.append(curr)
                for adjv in self.E[curr]:
                    degree[adjv]-=1
                    if degree[adjv]==0:
                        Q.append(adjv)
        else:
            Q=deque([u for u in degree if degree[u]==1])
            while Q:
                print("degree:",degree)
                curr=Q.popleft()
                print("curr:",curr)
                seq.append(curr)
                for adjv in self.E[curr]:
                    degree[adjv]-=1
                    if degree[adjv]==1:
                        Q.append(adjv)
                    

        if len(seq)!=len(self.V):
            return None
        else:
            return seq
if __name__=="__main__":
    '''
    V=set({0,1,2,3,4,5,6,7,8,9})
    E={ 0:[],
        1:[2,4,5],
        2:[3],
        3:[1],
        4:[6,7],
        5:[4,6,7],
        6:[9],
        7:[9],
        8:[],
        9:[],
    }
    g=Graph(V,E)
    g.BFS(1)
    g.DFS(1)
    print(g.standardRecursiveDFS(1))
    print(g.standardDFS(1))
    print(g.standardBFS(1))
    '''
    '''
    V=set(['a','b','c','d','e','f'])
    E={
        "a":set(['b','f']),
        "b":set(['c','d','f']),
        "c":set(['d']),
        "d":set(['e','f']),
        "e":set(['f']),
        "f":set([]),
    }
    '''
    V=set(['a','b','c','d','e','f'])
    E={
        "a":set(['b','c','d','e']),
        "b":set(['a']),
        "c":set(['a']),
        "d":set(['a']),
        "e":set(['a','f']),
        "f":set(['e']),
    }
    g=Graph(V,E)
    print(g.quickBFS('a'))
    #print(g.calcDegree())
    #print(g.standardTopologySort(False))