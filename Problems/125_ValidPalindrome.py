class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerstr=s.lower()
        alphanumeric_filter = filter(str.isalnum, lowerstr)
        alphanumeric_string = "".join(alphanumeric_filter)
        return self.checkPalindrome(alphanumeric_string)

    def checkPalindrome(self,lowerstr):
        if len(lowerstr)==0:
            return True
        flag=True
        for i in range(len(lowerstr)//2):
            if lowerstr[i]!=lowerstr[len(lowerstr)-1-i]:
                flag=False
                break
        return flag