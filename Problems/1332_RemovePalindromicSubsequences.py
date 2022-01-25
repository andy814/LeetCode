class Solution:
    def removePalindromeSub(self, s: str) -> int:
        sList=list(s)
        count=0
        while sList:
            count+=1
            toRemove=[ char for i,char in enumerate(sList) if sList[i]==sList[-1-i]]
            print(sList)
            print(sList[1])
            print(sList[-2])
            for char in toRemove:
                sList.remove(char)
        return count

print(Solution().removePalindromeSub("abb"))
print(Solution().removePalindromeSub("abb"))