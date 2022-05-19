#source: https://github.com/azl397985856/leetcode/blob/master/problems/229.majority-element-ii.md
# select elements that appears more than n//3 times
def majorityElement(nums):
    c1 = c2 = 0
    v1 = v2 = -1

    for num in nums:
        if num == v1: c1 += 1
        elif num == v2: c2 += 1
        elif c1 == 0:
            c1 = 1
            v1 = num
        elif c2 == 0:
            c2 = 1
            v2 = num
        else:
            c1 -= 1
            c2 -= 1
    # check
    c1 = c2 = 0
    for num in nums:
        if v1 == num: c1 += 1
        if v2 == num: c2 += 1
    ans = []
    if c1 > len(nums)//3: ans.append(v1)
    if c2 > len(nums)//3: ans.append(v2)
    return list(set(ans))