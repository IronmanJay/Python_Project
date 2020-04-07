"""
问题：
输出9*9口诀
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d "%(j,i,j*i),end=' ')
    print(' ')