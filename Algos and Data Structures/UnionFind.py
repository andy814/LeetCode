class UnionFind():
    def __init__(self,n):
        self.p=list(range(n))
        self.rank=[1]*n
    
    def find(self,i):
        if i!=self.p[i]:
            self.p[i]=self.find(self.p[i])
        return self.p[i]

    def union(self,i,j): # or you can return False/True to check whether they are connected
        rooti=self.find(i)
        rootj=self.find(j)

        if rooti==rootj:
            return # or return False, used for Kruskal

        if self.rank[rooti]>self.rank[rootj]:
            self.p[rootj]=rooti
        elif self.rank[rooti]<self.rank[rootj]:
            self.p[rooti]=rootj
        else:
            self.p[rootj]=rooti
            self.rank[rooti]+=1

        # add return True when using Kruskal
