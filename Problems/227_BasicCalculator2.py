from typing import *
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        temp=s.replace("-","+")
        temp=temp.replace("*","+")
        temp=temp.replace("/","+")
        nums=temp.split("+")
        nums=[int(num) for num in nums]
        ops=[]
        opSet=["+","-","*","/"]
        for ch in s:
            if ch in opSet:
                ops.append(ch)
        stack=[nums[0]]
        numsPtr=1
        opsPtr=0
        #print(ops)
        #print(nums)
        while numsPtr<len(nums):
            #print(opsPtr,numsPtr)
            if ops[opsPtr]=="+" or ops[opsPtr]=="-":
                stack.append(ops[opsPtr])
                stack.append(nums[numsPtr])
            else:
                lastNum=stack.pop()
                #print(lastNum,nums[numsPtr],numsPtr)
                if ops[opsPtr]=="*":
                    stack.append(lastNum*nums[numsPtr])
                else:
                    stack.append(lastNum//nums[numsPtr])
            numsPtr+=1
            opsPtr+=1
        
        stack=deque(stack)
        while len(stack)>1:
            num1=stack.popleft()
            ops=stack.popleft()
            num2=stack.popleft()
            if ops=="+":
                stack.appendleft(num2+num1)
            elif ops=="-":
                stack.appendleft(num2-num1)

        return stack[0]        

        