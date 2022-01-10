from collections import deque

def BFS(V,E,s):
    queue=deque()
    visited={}
    for v in V:
        visited[v]=False
    #visited[s]=True
    queue.append(s)
    print("BFS:",end=" ")
    while queue:
        curr=queue.popleft()
       # print(curr,end=" ")
        if visited[curr]==False:
            print(curr,end=" ")
            visited[curr]=True
            for adjV in E[curr]:
                if visited[adjV]==False: #加这一句提升一点效率，但是不影响正确性
                    queue.append(adjV)

def DFS(V,E,src):
    stack=deque()
    visited=[]
    stack.append(src)
    print("DFS: ",end=" ")
    while stack:
        curr=stack.pop()
        if curr not in visited:
            visited.append(curr)
            print(curr,end=" ")
            for adjV in E[curr]:
                if adjV not in visited:
                    stack.append(adjV)

def recursiveDFS(V,E,src,visited=None):
    if not visited:
        print("recursiveDFS:",end=" ")
        visited=[]
    if src not in visited:
        print(src,end=" ")
        visited.append(src)
        for adjV in E[src]:
            #if adjV not in visited:
            recursiveDFS(V,E,adjV,visited)

def DFS2(V,E,src):
    stack=deque()
    visited=[]
    stack.append(src)
    print("DFS: ",end=" ")
    while stack:
        curr=stack.pop()    
        print(curr,end=" ")
        for adjV in E[curr]:
            if adjV not in visited:
                visited.append(adjV)
                stack.append(adjV)

def recursiveDFS2(V,E,src,visited=None):
    if not visited:
        print("recursiveDFS:",end=" ")
        visited=[src]
    print(src,end=" ")
    #visited.append(src)
    for adjV in E[src]:
        if adjV not in visited:
            visited.append(adjV)
            recursiveDFS2(V,E,adjV,visited)
            
if __name__=="__main__":
    V={0,1,2,3,4,5}
    E={
    0:[],
    1:[2,4],
    2:[3],
    3:[4],
    4:[],
    5:[]
    }
    DFS2(V,E,1)