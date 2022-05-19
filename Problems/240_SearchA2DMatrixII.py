from typing import *
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisearch(row,target):
            start=0
            end=len(row)
            while start<=end:
                mid=(start+end)//2
                if row[mid]==target:
                    return True
                elif row[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return False
        
        for i,row in enumerate(matrix):
            if bisearch(row,target):
                return True
        return False


