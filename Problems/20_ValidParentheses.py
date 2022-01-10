# Stack
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        flag=True
        stack=deque()
        for i in range(len(s)):
            curr=s[i]
            if curr == "(" or curr == "[" or curr == "{":
                stack.append(curr)
            elif curr == ")" or curr == "]" or curr == "}":
                if not stack:
                    return False
                top=stack.pop()
                if top == "(":
                    if curr != ")":
                        flag=False
                        break
                if top == "[":
                    if curr != "]":
                        flag=False
                        break
                if top == "{":
                    if curr != "}":
                        flag=False
                        break
        if stack:
            flag=False
        return flag

s=Solution()
print(s.isValid("[]"))
