def binarySearch(aa,target): # aa: non-decreasing array, return the index of target
    start=0
    end=len(aa)-1
    while start<=end:
        mid=(start+end)//2
        if aa[mid]<target:
            start=mid+1
        elif aa[mid]>target:
            end=mid-1
        else:
            return mid
    return -1