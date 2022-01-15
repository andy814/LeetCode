from typing import *
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record=set()
        for i in range(min(k+1,len(nums))): # pitfall
            if nums[i] in record:
                return True
            record.add(nums[i])
        for i in range(k+1,len(nums)):
            record.remove(nums[i-k-1])
            if nums[i] in record:
                return True
            record.add(nums[i])
        return False

sol=Solution()
sol.containsNearbyDuplicate([1,0,1,1],1)