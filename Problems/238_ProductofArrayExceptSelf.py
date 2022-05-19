from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # extra space
        prefixProduct=[]
        suffixProduct=[]
        prod=1
        for num in nums:
            prod*=num
            prefixProduct.append(prod)
        prod=1
        for num in nums[::-1]:
            prod*=num
            suffixProduct.append(prod)
        suffixProduct=suffixProduct[::-1]
        ans=[]
        for i,num in nums:
            if i==0:
                ans.append(suffixProduct[1])
            elif i==len(nums)-1:
                ans.append(prefixProduct[i-1])
            else:
                ans.append(prefixProduct[i-1]*suffixProduct[i+1])
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixProduct=[]
        temp=1
        for num in nums[::-1]:
            temp*=num
            suffixProduct.append(temp)
        suffixProduct=suffixProduct[::-1]
        prefixProd=1
        for i,num in enumerate(nums):
            if i==0:
                suffixProduct[i]=suffixProduct[1]
            elif i==len(nums)-1:
                suffixProduct[i]=prefixProd
            else:
                suffixProduct[i]=suffixProduct[i+1]*prefixProd
            prefixProd*=num
        return suffixProduct
