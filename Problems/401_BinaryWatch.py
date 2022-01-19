from typing import *
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        #possibleH=[1,2,4,8]
        #possibleM=[1,2,4,8,16,32]
        hourDict={}
        minuteDict={}
        hourDict[0]=[0]
        hourDict[1]=[1,2,4,8]
        hourDict[2]=[3,5,9,6,10]
        hourDict[3]=[7,11]

        minuteDict[0]=[0]
        minuteDict[1]=[1,2,4,8,16,32]
        minuteDict[2]=[3,5,9,17,33,6,10,18,34,12,20,36,24,40,48]
        minuteDict[3]=[7,11,19,35,13,21,37,25,41,49,14,22,38,26,42,50,28,44,52,56]
        minuteDict[4]=[63-i for i in minuteDict[2][1:] ]
        minuteDict[5]=[59,55,47,31]

        ret=[]
        for i in range(turnedOn+1):
            j=turnedOn-i
            if i not in hourDict or j not in minuteDict:
                continue
            for h in hourDict[i]:
                for m in minuteDict[j]:
                    ret.append(self.getFormat(h,m))        
        return ret
    
    def getFormat(self,hour,minute):
        if hour>11 or hour<0:
            raise Exception("invalid hour")

        if minute>59 or minute<0:
            raise Exception("invalid minute")

        hourStr=str(hour)
        minStr=""
        if minute==0:
            minStr="00"
        elif minute<10 and minute>0:
            minStr="0"+str(minute)
        else:
            minStr=str(minute)

        return hourStr+":"+minStr
                    

class Solution2:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret=[]
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count("1")==turnedOn:
                    ret.append(str(i)+":"+str(j).rjust(2,"0"))
        return ret
