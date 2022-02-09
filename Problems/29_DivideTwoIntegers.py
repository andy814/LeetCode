class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend==0:
            return 0

        negFlag=1
        upperBound=2**31-1
        lowerBound=-2**31
        
        if dividend<0:
            negFlag=0-negFlag
            dividend=0-dividend
        if divisor<0:
            negFlag=0-negFlag
            divisor=0-divisor
        
        if divisor==1:
            if negFlag==1:
                ans=dividend
            else:
                ans=0-dividend
            if lowerBound<=ans<=upperBound:
                return ans
            elif ans<lowerBound:
                return lowerBound
            else:
                return upperBound

        expo=1
        curr=divisor
        while curr<=dividend:
            expo+=1
            curr=divisor**expo
        expo-=1
        ret=[]
        
        while expo>0:
            posDiv=0
            while dividend>=divisor**expo:
                dividend-=divisor**expo
                posDiv+=1
            ret.append(posDiv)
            expo-=1 # ret=12

        ans=0
        for i,num in enumerate(ret):
            single=divisor**(len(ret)-i-1)
            while num>0:
                ans+=single
                num-=1
        
        if negFlag==-1:
            ans=0-ans
        
        if lowerBound<=ans<=upperBound:
            return ans
        elif ans<lowerBound:
            return lowerBound
        else:
            return upperBound