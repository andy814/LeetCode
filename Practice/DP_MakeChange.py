
def DP(coins, m, s):
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for i in range(len(coins)):
        for j in range(m, coins[i]-1, -1):
            for k in range(1, s[i]+1):  # 枚举每个硬币的个数 [1, s[i]]
                if j >= k*coins[i]:  # 确保不超过金额 j
                    f[j] = min(f[j], f[j - k*coins[i]] + k)
    print(f[-1])
    return -1 if f[m] > m else f[m]

def MinTuple(coins,m):
    M=[float('inf')]*(m+1)
    tuple=[]
    for i in range(len(M)):
        tuple.append([0]*len(coins))
    for i in range(len(M)):
        if i==0:
            M[i]=0
        else:
            for j in range(len(coins)):
                if i>=coins[j]:
                    if M[i]>1+M[i-coins[j]]:
                        M[i]=1+M[i-coins[j]]
                        tuple[i]=tuple[i-coins[j]].copy()
                        tuple[i][j]+=1
    return tuple[m],M[m]

def MinTuple2(coins,m):
    amount=[0]*len(coins) # 改成inf
    for i in range(len(coins)):
        for j in range(m//coins[i]+1):
            if MinTuple(coins,m-j*coins[i])[1]+j==MinTuple(coins,m)[1]:
                amount[i]=j
        m=m-amount[i]*coins[i] #改正
    return amount





coins=[1,12,28,114]
m=112
s=[4,6,3,0]

#coins=[1,2,3,4]
#m=6

#print("multest:",MinTuple(coins,4))

#DP(coins,m,s)
print(MinTuple(coins,m))
print(MinTuple2(coins,m))