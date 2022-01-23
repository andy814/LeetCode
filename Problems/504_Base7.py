import collections
class Solution:
    def convertToBase7(self, num: int) -> str:
        isNeg=False
        if num==0:
            return 0
        if num<0:
            isNeg=True
            num=-num
        ret=[]
        div=1
        while div*7<=num:
            div*=7
        while div>0:
            ret.append(num//div)
            num-=ret[0]*div
            div/=7
        retStr="-" if isNeg else ""
        for i in ret:
            retStr+=str(i)
        return retStr

    def convertToBase7_2(self, num: int) -> str:
        if num==0:
            return "0"
        ret=collections.deque()
        isNeg=True if num<0 else False
        num=abs(num)
        while num>0:
            num,remain=num//7,num%7
            ret.appendleft(str(remain))
        return "-"+"".join(ret) if isNeg else "".join(ret)

