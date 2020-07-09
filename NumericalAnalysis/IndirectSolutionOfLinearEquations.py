
#平方根法
import numpy as np
A=[[4,2,4],[2,10,-1],[4,-1,6]]
b=[[4,17,0]]
print (len(A))
k=0
def get_under(A):#获取A的下三角矩阵
    Under=list(np.zeros((len(A),len(A))))
    for i in A:
        x=A.index(i)
        n=0
        for t in i:
            if n<=x:
                Under[x][n]=A[x][n]
            n=n+1
    d=[]
    for i in Under:
        d.append((list(i)))
    return d

def get_base(m):#给一个矩阵为基，在这个基上修改得到我们的答案
    base=list(np.zeros((len(A),len(A))))
    return base

def get_GT_D(a,base,k):#对于对角线上的元素有这样的算法
    m=0
    sum1=0.00000000000
    while m < k:
        sum1=sum1+(base[k][m])**2
        m=m+1
    base[k][k]=(a[k][k]-sum1)**(0.5000000000)
    return base

def get_GT_ND(a,base,i,k):#对于非对角线上的元素有这样的解法，应该可以和上面一部分并在一块
    if i==k:
        return base
    else:
        sum1=0.0000000000000
        m=0
        if k-1<0:
            base[i][k]=a[i][k]/base[k][k]
        else:
            while m<k:
                sum1=sum1+base[i][m]*base[k][m]
                m=m+1
            base[i][k]=(a[i][k]-sum1)/base[k][k]
        return base

def get_G(A):#导出我们需要的矩阵G
    a=get_under(A)
    base=get_base(A)
    base[0][0]=a[0][0]**0.50000000000
    n=[]
    for i in base:
        n.append(list(i))
    base=n
    i=0
    while i<len(A):
        k=0
        while k<i:
            get_GT_ND(a,base,i,k)
            k=k+1
        get_GT_D(a,base,k)
        i=i+1
    return base

def build_matrix(A,b):#通过这段代码导出增广矩阵
    B=[]
    for i in A:
        n=A.index(i)
        i.append(b[0][n])
        B.append(i)
    return B

def solve_lower(A,b):#解线性方程组的第一种方法，这里是Gy=b，顺序gauss消去法解出y
    B=build_matrix(get_G(A),b)
    C=[]
    for i in B:
        C.append(np.array(i))
    k=0
    while k<len(A):
        for i in range(k+1,len(A)):
            C[i]=C[i]-C[k]*B[i][k]/B[k][k]
        k=k+1
    D=[]
    for i in C:
        D.append(list(i))
    ans=[]
    for i in D:
        for j in i:
            if j==0:
                pass
            else:
                ans.append(i[-1]/j)
                break
    ans1=[]
    ans1.append(ans)
    return ans1

b= solve_lower(A,b)
N=np.mat(get_G(A)).T
ee=np.mat(b).T
print (N.I*ee) #解线性方程组的第二种方法，将系数矩阵的逆矩阵左乘到方程右端
