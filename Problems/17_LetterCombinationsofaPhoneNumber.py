from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        mapping=\
        {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        def recurFunc(digits):
            nonlocal mapping
            if len(digits)==1:
                return mapping[digits[0]]
            else:
                recur=recurFunc(digits[:-1])
                ret=[]
                lastDigit=digits[-1]
                for seq in recur:
                    for letter in mapping[lastDigit]:
                        ret.append(seq+letter)
                return ret
        return recurFunc(digits)


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        mapping=\
        {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        res=product([mapping[num] for num in digits])
        return [list(tup) for tup in res]

class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mapping=[" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res=product( *[mapping[int(num)] for num in digits] )
        return [ "".join(tup) for tup in res]
        
