from typing import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # time: beat 68.09%, space: O(n)
        diff={}
        for i in range(len(numbers)):
            if numbers[i] in diff:
                return [diff[numbers[i]]+1,i+1]
            diff[target-numbers[i]]=i

    def twoSumTwoPtrs(self, numbers: List[int], target: int) -> List[int]: # time: beat 28.91%, space: O(1)
        front=0
        rear=len(numbers)-1
        while True:
            if numbers[front]+numbers[rear]==target:
                return [front+1,rear+1]
            elif numbers[front]+numbers[rear]<target:
                front+=1
            elif numbers[front]+numbers[rear]>target:
                rear-=1
