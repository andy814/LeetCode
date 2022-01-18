from logging import raiseExceptions
import sys
encodeBits=12
class Solution:

    def getSumPositive(self, a: int, b: int) -> int: # deal with positives only

        aBin=bin(a)[2:]
        bBin=bin(b)[2:]
        diff=len(aBin)-len(bBin)
        maxlen=max(len(aBin),len(bBin))
        if diff>0:
            bBin="0"*diff+bBin
        else:
            aBin="0"*diff+aBin

        ret=[0]*(maxlen+1)
        carry="0"

        for i in range(maxlen-1,-1,-1):
            num1=[aBin[i],bBin[i],carry].count("1")
            if num1==0:
                ret[i+1]=0
                carry="0"
            elif num1==1:
                ret[i+1]=1
                carry="0"
            elif num1==2:
                ret[i+1]=0
                carry="1"
            elif num1==3:
                ret[i+1]=1
                carry="1"
            else:
                raise Exception("exception occurs") 

        if carry=="1":
            ret[0]="1"

        retNbr=int(ret,2)
        return retNbr

    def encode(self,decimal) -> str: # encode 12 bits
        binDecimal=bin(decimal)
        
        if binDecimal[0]=="-":
            temp=binDecimal[3:] 
            temp="0"*(encodeBits-len(temp))+temp            
            #ret=["0"]*encodeBits
            ret=[char for char in temp]
            met1=False
            for i in range(encodeBits-1,-1,-1):
                if met1:
                    if temp[i]=="1":
                        ret[i]="0"
                    else:
                        ret[i]="1"
                if temp[i]=="1":
                    met1=True
            retStr=""
            for i in ret:
                retStr+=i
            return retStr

        else:
            ret=binDecimal[2:]
            ret="0"*(encodeBits-len(ret))+ret
            return ret

    def decode(self,comp)->int: #return decimal
        if comp[0]=="0":
            return int(comp,2)
        else:
            #ret=["0"]*encodeBits
            ret=[char for char in comp]

            met1=False
            #print(comp)
            for i in range(encodeBits-1,-1,-1):
                #print(ret)
                if met1:
                    if comp[i]=="1":
                        ret[i]="0"
                    else:
                        ret[i]="1"
                if comp[i]=="1":
                    met1=True
            retStr=""
            for i in ret:
                retStr+=i
            return (-1)*(int(retStr,2))

    def add(self,aComp,bComp)->str:
        carry="0"
        ret=["0"]*encodeBits
        for i in range(encodeBits-1,-1,-1):
            num1=[aComp[i],bComp[i],carry].count("1")
            if num1==0:
                ret[i]="0"
                carry="0"
            elif num1==1:
                ret[i]="1"
                carry="0"
            elif num1==2:
                ret[i]="0"
                carry="1"
            elif num1==3:
                ret[i]="1"
                carry="1"
            else:
                raise Exception("exception occurs") 
        
        # if carry=="1":
        #     ret[0]="1"

        retStr=""
        for i in ret:
            retStr+=i
        
        return retStr

    def getSum(self, a: int, b: int) -> int:
        encodedA=self.encode(a)
        encodedB=self.encode(b)
        #print(encodedA,encodedB)
        suminComp=self.add(encodedA,encodedB)
        ret=self.decode(suminComp)
        return ret

class Solution2:

    def twos(self,val):
        b=val.to_bytes(4,byteorder=sys.byteorder,signed=False)
        return int.from_bytes(b,byteorder=sys.byteorder,signed=True)

    def getSum(self, a: int, b: int) -> int:
        a=a&0xFFFFFFFF
        b=b&0xFFFFFFFF
        carry=0
        while b:
            carry=a&b
            a=a^b
            b=(carry<<1)&0xFFFFFFFF

        return self.twos(a)
        #if a&(1<<31)==1:
            #return 
        #return a

    def getComp(self,a):
        if a>=0:
            return bin(a)[2:]
        else:
            return bin(~(-a-1))

sol=Solution2()
print(sol.getComp(-5))
print(bin(-5&0xFFFFFFFF))