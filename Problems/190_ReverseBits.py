class Solution:
    def reverseBits(self, n: int) -> int:
        
        binaryN=bin(n)[2:]
        num0=32-len(binaryN)
        reversedBinaryN=binaryN[::-1]
        ret=reversedBinaryN+"0"*num0
        return int(ret,2)

        
        #for i in range(len(binaryN)//2):
        #    binaryN[i],binaryN[len(binaryN)-i-1]=binaryN[len(binaryN)-i-1],binaryN[i]