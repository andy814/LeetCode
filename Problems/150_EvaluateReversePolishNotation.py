from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token!="+" and token!="-" and token!="*" and token!="/":
                stack.append(token)
            else:
                opr2=int(stack.pop())
                opr1=int(stack.pop())
                if token=="+":
                    stack.append(opr1+opr2)
                elif token=="-":
                    stack.append(opr1-opr2)
                elif token=="*":
                    stack.append(opr1*opr2)
                elif token=="/":
                    stack.append(opr1//opr2)
        return stack[0]
                
