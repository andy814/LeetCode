from functools import cache
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity>jug1Capacity+jug2Capacity:
            return False
        
        if jug1Capacity==jug2Capacity:
            return targetCapacity==jug1Capacity or targetCapacity==jug1Capacity*2
        
        if jug1Capacity==targetCapacity or jug2Capacity==targetCapacity or jug1Capacity+jug2Capacity==targetCapacity:
            return True
        
        max2=max(jug1Capacity,jug2Capacity)
        min2=min(jug1Capacity,jug2Capacity)
        jug1Capacity=max2
        jug2Capacity=min2

        # 最多只可能有一个半满！
        # 因此，将半满清空一定是错的！要么倒到另一个里面，要么被另一个倒！
        @cache
        def recur(left,right):
            nonlocal jug1Capacity,jug2Capacity,targetCapacity
            if left>jug1Capacity or right>jug2Capacity or left<0 or right<0:
                return False    
            if left==targetCapacity or right==targetCapacity or left+right==targetCapacity:
                return True
        
        # 往下则是半满的验证(不会了)
        if targetCapacity<jug2Capacity:
            return recur() or recur()
        elif jug2Capacity<targetCapacity<jug1Capacity:
            return recur() or recur()
        else:
            return recur() or recur()

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool: # sometimes TLE
        x=jug1Capacity
        y=jug2Capacity
        t=targetCapacity
        visited=set()
        def recur(l,r):
            visited.add((l,r))
            if l==t or r==t or l+r==t:
                return True

            n1=(0,r)
            n2=(l,0)
            n3=(x,r)
            n4=(l,y)
            n5=(l+r,0) if x-l>=r else (x,l+r-x)
            n6=(0,l+r) if y-l>=r else (l+r-y,y)

            next=[n1,n2,n3,n4,n5,n6]
            for n in next:
                if n not in visited:
                    if recur(n[0],n[1]):
                        return True
            return False
        return recur(0,0)