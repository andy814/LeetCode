import random

def insertionSort(aa): #最优复杂度n^2
    for i in range(1,len(aa)):
        for j in range(0,i):
            if aa[j]>aa[i]:
                aa.insert(j,aa[i])
                del aa[i+1]
                break
    return aa

def correctInsertionSort(aa): #最优复杂度是n
    for i in range(1,len(aa)):
        curr=aa[i]
        j=i-1
        while j>=0 and aa[j]>curr:
            aa[j+1]=aa[j]
            j-=1
        aa[j+1]=curr
    return aa

def selectionSort(aa):
    for i in range(len(aa)):
        minidx=i
        for j in range(i+1,len(aa)):
            if (aa[j]<aa[minidx]):
                minidx=j
        temp=aa[minidx]
        aa[minidx]=aa[i]
        aa[i]=temp
    return aa

def selectionSort2(aa):
    for i in range(len(aa)):
        minidx=aa[i:].index(min(aa[i:]))+i
        temp=aa[minidx]
        aa[minidx]=aa[i]
        aa[i]=temp
    return aa

def bubbleSort(aa): #最好情况n^2
    for i in range(len(aa)-1):
        for j in range(len(aa)-i-1):
            curr=aa[j]
            if(aa[j]>aa[j+1]):
                aa[j]=aa[j+1]
                aa[j+1]=curr
    return aa

def correctBubbleSort(aa): #最好情况n
    for i in range(len(aa)):
        sorted=True
        for j in range(len(aa)-i-1):
            if(aa[j]>aa[j+1]):
                aa[j],aa[j+1]=aa[j+1],aa[j]
                sorted=False
        if sorted==True:
            break
    return aa

def quickSort(aa,start,end): # start=0 , end=last index
    if start>end:
        return None
    pos=quickSortSub(aa,start,end)
    quickSort(aa,start,pos-1)
    quickSort(aa,pos+1,end)
    return aa

def quickSortSub(aa,start,end):
    pivot=aa[end]
    i=start
    for j in range(start,len(aa)):
        if aa[j]<pivot:
            aa[i],aa[j]=aa[j],aa[i]
            i+=1
    aa[i],aa[end]=aa[end],aa[i]
    return i

def simpleQuickSort(aa):
    if len(aa)<2:
        return aa
    low,same,high=[],[],[]
    pivot=aa[random.randint(0,len(aa)-1)]
    for e in aa:
        if e<pivot:
            low.append(e)
        elif e==pivot:
            same.append(e)
        else:
            high.append(e)
    return simpleQuickSort(low)+same+simpleQuickSort(high)

def mergeSort(aa,start,end):
    if end-start==0:
        return aa
    mid=start+(end-start)//2
    mergeSort(aa,start,mid)
    mergeSort(aa,mid+1,end)
    merge(aa,start,end)
    return aa

def merge(aa,start,end):
    mid=start+(end-start)//2
    merge1=aa[start:mid+1]
    merge2=aa[mid+1:end+1]
    i,j,curr=0,0,0
    while True:
        if i>=len(merge1):  
            aa[start+curr:end+1]=merge2[j:]
            return
        if j>=len(merge2): 
            aa[start+curr:end+1]=merge1[i:]
            return
        if merge1[i]<merge2[j]:
            aa[start+curr]=merge1[i]
            i+=1
            curr+=1
        else:
            aa[start+curr]=merge2[j]
            j+=1
            curr+=1

def bucketSort(aa,numbuckets): #但只能收正数
    buckets=[[] for i in range(numbuckets+1)]
    maxnbr=max(aa)
    minnbr=min(aa)
    for i in range(len(aa)):
        buckets[(int)((aa[i]-minnbr)*numbuckets/(maxnbr-minnbr))].append(aa[i])
    for i in range(numbuckets):
        buckets[i].sort()
    curr=0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            aa[curr]=buckets[i][j]
            curr+=1
    return aa

def shellSort(aa):
    gap=len(aa)//2
    while gap>0:
        for i in range(gap,len(aa)):
            curr=aa[i]
            j=i-gap
            while j>=0 and aa[j]>curr:
                aa[j+gap]=aa[j]
                j-=gap
            aa[j+gap]=curr
        gap//=2
    return aa

def countSort(aa):
    maxNbr=max(aa)
    minNbr=min(aa)
    bb=[0]*(maxNbr-minNbr+1)
    for i in range(len(aa)):
        bb[aa[i]-minNbr]+=1
    count=0
    for i in range(len(bb)):
        for j in range(bb[i]):
            aa[count]=i+minNbr
            count+=1
    return aa

def radixSort(aa):
    exp=1
    maxNbr=max(aa)
    while exp<maxNbr:
        bb=[[] for i in range(10)]
        for i in range(len(aa)):
            bb[(aa[i]//exp)%10].append(aa[i]) #分桶
        curr=0
        for i in range(len(bb)): #放回去
            for j in range(len(bb[i])):
                aa[curr]=bb[i][j]
                curr+=1
        exp*=10
    return aa

class Heap: 
    def __init__(self,aa): # 构造最小堆
        self.treeArray=[]
        for i in aa:
            self.add(i)
    
    def add(self,element):
        curr=len(self.treeArray)
        self.treeArray.append(element)
        while curr!=0:
            parent=(curr-1)//2
            if self.treeArray[curr]>=self.treeArray[parent]:
                break
            self.treeArray[curr],self.treeArray[parent]=self.treeArray[parent],self.treeArray[curr]
            curr=parent

    def top(self):
        if len(self.treeArray)==1:
            return self.treeArray[0]
        curr=0
        topelement=self.treeArray[curr]
        self.treeArray[0]=self.treeArray[-1]
        del self.treeArray[-1]
        while curr*2+1<=len(self.treeArray)-1:
            if curr*2+1==len(self.treeArray)-1: # only one child
                if self.treeArray[curr*2+1]<self.treeArray[curr]:
                    self.treeArray[curr*2+1],self.treeArray[curr]=self.treeArray[curr],self.treeArray[curr*2+1]
                return topelement
            else: # two children
                child1=self.treeArray[curr*2+1]
                child2=self.treeArray[curr*2+2]
                if self.treeArray[curr]<=min(child1,child2):
                    return topelement
                else:
                    if child1<child2:
                        self.treeArray[curr*2+1],self.treeArray[curr]=self.treeArray[curr],self.treeArray[curr*2+1]
                        curr=curr*2+1
                    else:
                        self.treeArray[curr*2+2],self.treeArray[curr]=self.treeArray[curr],self.treeArray[curr*2+2]
                        curr=curr*2+2
        return topelement

    def heapSort(self):
        ret=[]
        treeArr=self.treeArray[:]
        for i in range(len(treeArr)):
            ret.append(self.top())
        return ret

def heapSort(aa):
    print("heap(aa):",Heap(aa).treeArray)
    return Heap(aa).heapSort()

def heapify(aa,n,i):#这里是最大堆,n=len(aa)
    child1=2*i+1
    child2=2*i+2
    maxidx=i
    if child1<n:
        if aa[child1]>aa[maxidx]:
            maxidx=child1
    if child2<n:
        if aa[child2]>aa[maxidx]:
            maxidx=child2
    if maxidx!=i:
        aa[maxidx],aa[i]=aa[i],aa[maxidx]
        heapify(aa,n,maxidx)

def correctHeapSort(aa):
    for i in range(len(aa)-1,-1,-1):
        heapify(aa,len(aa),i)
    for i in range(len(aa)-1,-1,-1):
        aa[i],aa[0]=aa[0],aa[i]
        heapify(aa,i,0)
    return aa

if __name__=="__main__":
    #aa=[1,3,3,5,2,4]
    aa=[1,33,34,33,5,2,4]
    bb=correctHeapSort(aa)
    print(bb)

