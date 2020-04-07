"""
问题：
打印杨辉三角
"""

def YangHuiSanJiao(n):
    L1 = [1]
    L2 = [1,1]
    print(L1)
    print(L2)

    i = 3

    while i < n:
        L = list(range(0,i))
        L[0] = 1
        L[i-1] = 1
        for j in range(1,i-1):
            L[j] = L2[j] + L2[j-1]
        i = i + 1
        L2 = L
        print(L)

YangHuiSanJiao(5)