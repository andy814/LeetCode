from typing import List
'''
class Solution: # O((m+n)log(m+n)) , 98% faster
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,m+n,1):
            nums1[i]=nums2[i-m]
        nums1.sort()
'''
       
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m+n-1
        p1=m-1
        p2=n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1]<nums2[p2]:
                nums1[i]=nums2[p2]
                p2-=1
            else:
                nums1[i]=nums1[p1]
                p1-=1
            i-=1
        while i >=0:
            if p1<0:
                nums1[i]=nums2[p2]
                i-=1
                p2-=1
            if p2<0:
            #nums1=nums2.copy()
            #print("nums1:",nums1)
                return
        


nums1=[2,0]
nums2=[1]
m=1
n=1
Solution().merge(nums1,m,nums2,n)
print(nums1)
        