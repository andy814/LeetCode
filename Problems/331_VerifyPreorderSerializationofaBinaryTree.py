class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        signs=preorder.split(",")
        if signs[0]=="#":
            return False if len(signs)>1 else True
        
        count=1
        for i,sign in enumerate(signs):
            if sign=="#":
                count-=1

            else:
                count+=1
                
            if count==0:
                return True if i==len(signs)-1 else False
            
            if count<0:
                return False
                
        return True if count==0 else False