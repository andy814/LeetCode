from typing import *
from xmlrpc.client import FastMarshaller
class Solution:
    def maxArea(self, height: List[int]) -> int:
        front=len(height)-1
        rear=0
        maxArea=(rear-front)*min(height[rear],height[front])
        while rear<front:
            if height[rear]<height[front]:
                rear+=1
            else:
                front-=1
            maxArea=max(maxArea,(rear-front)*min(height[rear],height[front]))
        return maxArea