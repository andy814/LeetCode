from typing import *
class Solution1:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenNums=[num for i,num in enumerate(nums) if i%2==0]
        oddNums=[num for i,num in enumerate(nums) if i%2==1]
        evenNums.sort()
        oddNums.sort(reverse=True)

        ret=[]
        if len(evenNums)==len(oddNums):
            for i in range(len(evenNums)):
                ret.append(evenNums[i])
                ret.append(oddNums[i])
        else:
            for i in range(len(oddNums)):
                ret.append(evenNums[i])
                ret.append(oddNums[i])
            ret.append(evenNums[-1])

        return ret

class Solution:
    def smallestNumber(self, num: int) -> int:
        
        def findMin(num): # num is positive, return min rearrangement
            strNum=str(num)
            numList=[]
            for char in strNum:
                numList.append(int(char))
            numList.sort()
            for i,num in enumerate(numList):
                if num!=0:
                    numList[0],numList[i]=numList[i],numList[0]
                    break
            ret=""
            for num in numList:
                ret+=str(num)
            return int(ret)


        def findMax(num): # num is positive, return max rearrangement
            strNum=str(num)
            numList=[]
            for char in strNum:
                numList.append(int(char))
            numList.sort(reverse=True)
            ret=""
            for num in numList:
                ret+=str(num)
            return int(ret)

        if num==0:
            return 0

        elif num>0:
            return findMin(num)

        else:
            num*=-1
            return (-1)*findMax(num)

class Bitset: # num solution

    def __init__(self, size: int):
        self.size=size
        self.num=0
        self.num1=0

    #1<<ridx=2**ridx
    def fix(self, idx: int) -> None: # O(logn)
        ridx=idx
        if self.num&(1<<ridx)==0:
            self.num1+=1
            self.num|=1<<ridx

    def unfix(self, idx: int) -> None: # O(logn)
        ridx=idx
        if self.num&(1<<ridx)!=0:
            self.num1-=1
            self.num^=1<<ridx

    def flip(self) -> None: # O(logn)
        self.num1=self.size-self.num1
        self.num^=(1<<self.size)-1

    def all(self) -> bool: # O(1)
        return self.num1==self.size

    def one(self) -> bool: # O(1)
        return self.num1>0
        
    def count(self) -> int: # O(1)
        return self.num1

    def toString(self) -> str: # O(n)
        return bin(self.num)[2:].rjust(self.size,"0")

class Bitset: # list solution
    def __init__(self, size: int):
        #self.size=size
        self.nums=[0]*size
        self.flipNums=[1]*size
        self.num1=0 # record 1 in NUMS
        self.flipped=False

    def fix(self, idx: int) -> None: # O(1)
        if self.nums[idx]!=1:
            self.num1+=1
        self.nums[idx]=1
        self.flipNums[idx]=0

    def unfix(self, idx: int) -> None: # O(1)
        if self.nums[idx]!=0:
            self.num1-=1
        self.nums[idx]=0
        self.flipNums[idx]=1

    def flip(self) -> None: # O(1)
        self.num1=len(self.nums)-self.num1
        self.nums,self.flipNums=self.flipNums,self.nums

    def all(self) -> bool: # O(1)
        return self.num1==len(self.nums)

    def one(self) -> bool: # O(1)
        return self.num1>0

    def count(self) -> int: # O(1)
        return self.num1

    def toString(self) -> str:
        return "".join([str(num) for num in self.nums])


class Solution:
    def minimumTime(self, s: str) -> int:
        if len(s)==1:
            return int(s)
        
        s=[int(i) for i in s]
        minL=[s[0]]
        minR=[s[-1]]
        for i,num in enumerate(s[1:]):
            if num==0:
                minL.append(minL[-1])
            else:
                minL.append(min(minL[-1]+2,i+2))
        
        revS=s[::-1]
        for i,num in enumerate(revS[1:]):
            if num==0:
                minR.append(minR[-1])
            else:
                minR.append(min(minR[-1]+2,i+2))

        ret=float("inf")
        for i in range(len(s)-1):
            ret=min(ret,minL[i]+minR[len(s)-i-2])
        return ret