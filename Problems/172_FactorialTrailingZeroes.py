import time
class Solution:
    def trailingZeroes(self, n: int) -> int: # O(n)
        num2count,num5count=0,0
        for i in range(1,n+1):
            num2,num5=self.factorize(i)
            num2count+=num2
            num5count+=num5
        return min(num2count,num5count)

    def trailingZeroesLog(self, n: int) -> int: # O(log(n))
        # n/5+n/5^2+n/5^3+...
        count=0
        while n>=5:
            n//=5
            count+=n
        return count

    def factorize(self,i):
        temp=i
        num2,num5=0,0
        while temp%2==0:
            temp/=2
            num2+=1
        temp=i
        while temp%5==0:
            temp/=5
            num5+=1
        return num2,num5

sol=Solution()
print(sol.trailingZeroes(10))