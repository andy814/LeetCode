#source: https://blog.csdn.net/Dby_freedom/article/details/102144772

def dp_01(coins, m): # 找零问题，每个硬币只能选一次/01背包问题
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for c in coins:  # 逐个考虑硬币，这里两个for循环顺序不能反
        for j in range(m, c-1, -1):  # 只能从大到小枚举
            f[j] = min(f[j], f[j - c] + 1)
    return f[m] if f[m] != float('inf') else -1  

def dp_complete(coins, m): # 找零问题，硬币无限/完全背包问题
    f = [float('inf')]*(m+1)
    f[0] = 0
    for c in coins:  # 两个for循环也可以反过来，这样就变成对每个金额总量，分别考虑每个coin，思路更顺一些
        for j in range(c, m+1):  # 只能从小到大枚举
            f[j] = min(f[j], f[j - c] + 1) # 优化过程其实很复杂，所以看起来不直观
    return f[m] if f[m] != float('inf') else -1  

def dp_limited(coins, m, s): # 找零问题，每个硬币分别有s[i]枚/多重背包问题，每个物品只能取s[i]次
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for i in range(len(coins)):
        for j in range(m, coins[i]-1, -1): # 从大到小
            for k in range(1, s[i]+1):  # 枚举每个硬币的个数，保证别拿过头就行了
                if j >= k*coins[i]:  
                    f[j] = min(f[j], f[j - k*coins[i]] + k)
    return -1 if f[m] > m else f[m]