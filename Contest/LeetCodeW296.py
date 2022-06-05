from multiprocessing.dummy import current_process
from typing import *
from sortedcontainers import SortedList
class Solution1:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            n=len(nums)
            next=[0]*(n//2)
            for i in range(len(next)):
                next[i]=min(nums[i*2],nums[i*2+1]) if i%2==0 else max(nums[i*2],nums[i*2+1])
            nums=next
        return nums[0]

from sortedcontainers import SortedList
class Solution2:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if k==0:
            return len(set(nums))
        sortedList=SortedList(nums)
        #print(sortedList)
        ans=1
        currTop=sortedList[0]+k
        #print((currTop-k,currTop))
        while currTop<sortedList[-1]:
            nextElement=sortedList.bisect_right(currTop)
            ans+=1
            if currTop==sortedList[nextElement]: # try comment this one
                currTop=sortedList[nextElement]+k+1
            else:
                currTop=sortedList[nextElement]+k
            #print((currTop-k,currTop))
        return ans

class Solution3:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_idx=dict( (num,i) for (i,num) in enumerate(nums) )
        for ops in operations:
            idx=num_idx[ops[0]]
            nums[idx]=ops[1]
            del num_idx[ops[0]]
            num_idx[ops[1]]=idx
        return nums

class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class TextEditor:
    
    def __init__(self):
        #self.text=[]
        self.sentinel=Node("A")
        self.currPos=self.sentinel   
        
    def overview(self):
        curr=self.sentinel.right
        print("content:")
        while curr:
            print(curr.val+"->",end="")
            curr=curr.right
        record=self.currPos
        k=0
        while self.currPos.val!="A":
            k+=1
            self.currPos=self.currPos.left
        self.currPos=record
        print("")
        print("curr val,idx:",record.val,k)

    def addText(self, text: str) -> None:
        #print("command: addText,",text)
        record=self.currPos.right
        for ch in text:
            next=Node(ch)
            self.currPos.right=next
            next.left=self.currPos
            self.currPos=next        
        self.currPos.right=record
        if record:
            record.left=self.currPos
        #self.overview()
        

    def deleteText(self, k: int) -> int:
        #print("command: deleteText,",k)
        move=0
        record=self.currPos
        while move<k and self.currPos.val!="A":
            move+=1
            self.currPos=self.currPos.left
        if record.right:
            record.right.left=self.currPos
            self.currPos.right=record.right
        else:
            self.currPos.right=None
        #self.overview()
        return move

    def cursorLeft(self, k: int) -> str:
        #print("command: cursorLeft,",k)
        ret=[]
        move=0
        while move<k and self.currPos.val!="A":
            move+=1
            self.currPos=self.currPos.left

        move=0
        k=10
        record=self.currPos
        while move<k and self.currPos.val!="A":
            ret.append(self.currPos.val)
            move+=1
            self.currPos=self.currPos.left

        self.currPos=record
        ret=ret[::-1]
        #self.overview()
        return "".join( ch for ch in ret )

    def cursorRight(self, k: int) -> str:
        #print("command: cursorRight,",k)
        ret=[]
        move=0
        while move<k and self.currPos.right:
            move+=1
            self.currPos=self.currPos.right

        move=0
        k=10
        record=self.currPos
        while move<k and self.currPos.val!="A":
            ret.append(self.currPos.val)
            move+=1
            self.currPos=self.currPos.left

        self.currPos=record
        ret=ret[::-1]
        #self.overview()
        return "".join( ch for ch in ret )