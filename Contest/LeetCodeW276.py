from audioop import reverse
import collections
from typing import *

class Solution1:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret=[]
        while len(s)>k:
            ret.append(s[:k])
            s=s[k:]
        if len(s)==0:
            return ret
        else:
            ret.append(s+fill*(k-len(s)))
            return ret

class Solution2:
    def minMoves(self, target: int, maxDoubles: int) -> int: # DP, but memory exhausted
        # key=currval, value=(stepToGo,doubledTimes)
        visited=collections.defaultdict(lambda:(0,0))
        visited[target]=(0,0)
        visited[target-1]=(1,0)
        for i in range(target-2,0,-1):
            if i*2>target or visited[2*i][1]>=maxDoubles: # multiply not available
                step=visited[i+1][0]+1
                doubledTimes=visited[i+1][1]
                visited[i]=(step,doubledTimes)
                if i+1%2==1:
                    visited.pop(i+1)
            else:
                if visited[i+1][0]>visited[i*2][0]:
                    step=visited[i*2][0]+1
                    doubledTimes=visited[i*2][1]+1
                    visited.pop(i+1)
                else:
                    step=visited[i+1][0]+1
                    if i+1%2==1:
                        visited.pop(i+1)

                visited[i]=(step,doubledTimes)
        return visited[1][0]

    def minMoves(self, target: int, maxDoubles: int) -> int: # DP, but memory exhausted
        ret=0
        doubled=0
        while target>1 and doubled<maxDoubles:
            if target%2==0:
                target//=2
                ret+=1
                doubled+=1
            else:
                target-=1
                ret+=1
        return ret+target-1

class Solution3:
    def mostPoints(self, questions: List[List[int]]) -> int:
        visited=[0]*len(questions)
        for i in range(len(questions)-1,-1,-1):
            if i+questions[i][1]+1>=len(questions):
                if i==len(questions)-1:
                    visited[i]=questions[i][0]
                else:
                    visited[i]=max(visited[i+1],questions[i][0])
            else:
                visited[i]=max(visited[i+1],questions[i][0]+visited[ i+questions[i][1]+1 ] )
        return visited[0]


class Solution4:
    def maxRunTime(self, n: int, batteries: List[int]) -> int: # time limit exceeded
        count=0
        batteries.sort(reverse=True)
        while batteries[n-1]>0:
            batteries[:n]=[i-1 for i in batteries[:n]] 
            batteries.sort(reverse=True)   
            count+=1
        return count

    def maxRunTime2(self, n: int, batteries: List[int]) -> int: # nlogn
        batteries.sort()
        totalEnergy=sum(batteries)
        while batteries[-1]>totalEnergy//n:
            maxBattery=batteries.pop()
            n-=1
            totalEnergy=totalEnergy-maxBattery
        limit=totalEnergy//n
        return limit