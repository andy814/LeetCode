from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag=True
        i=len(digits)-1
        while flag:
            if digits[i]==9:
                digits[i]=0
                if i ==0:
                    digits.insert(0,1)
                    return digits
                else:
                    i-=1
            else:
                digits[i]+=1
                flag=False
        return digits

print(Solution().plusOne([0]))
            