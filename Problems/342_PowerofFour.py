class Solution:
    def isPowerOfFour(self, n: int) -> bool: # logn
        if n<=0:
            return False
        x=1
        while x<n:
            x*=4
        return x==n

    def isPowerOfFour2(self, n: int) -> bool: # logn
        if n<=0:
            return False
        binaryN=bin(n)[2:]
        if len(binaryN)<3: # at max 3
            return n==1
        met1=False
        if n&3==0: # end with 00
            for i in range(len(binaryN)-3,-1,-1):
                if binaryN[i]==1:
                    if (len(binaryN)-i)%2==0:
                        return False
                    else:
                        if met1:
                            return False
                        else:
                            met1=True
        return met1