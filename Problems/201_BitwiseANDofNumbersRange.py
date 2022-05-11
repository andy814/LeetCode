class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lBin=bin(left)[2:]
        ans=list(lBin)
        diff=right-left
        for i in range(len(lBin)):
            j=i+1
            lastNbr=int(lBin[-j:],2)
            if diff+lastNbr>=2**j:
                ans[-j]="0"
        resBin="".join(ch for ch in ans)
        return int(resBin,2)
