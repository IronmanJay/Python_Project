from __future__ import division
import numpy as np
import math

class elimination(object):
    def __init__(self,dim):
        self.epsilon=0.000000001
        self.process=1
        self.dim=dim
        self.A=np.ones((self.dim,self.dim))
        self.jk=np.zeros(self.dim,dtype=np.int)
        self.xx=np.ones(self.dim)

    def elim(self,k):
        if math.fabs(self.A[k,k])<self.epsilon:
            return 1
        for i in range(k+1,self.dim):
            self.A[i,k]=self.A[i,k]/self.A[k,k]
            for j in range(k+1,self.dim):
                self.A[i,j]=self.A[i,j]-self.A[i,k]*self.A[k,j]
            self.xx[i]=self.xx[i]-self.A[i,k]*self.xx[k]
        if self.process==1:
            for i in range(self.dim):
                for j in range(self.dim):
                    print(self.A[i,j],end=" "),
                print("| ",self.xx[i])
            print("\n")

    def back(self):
        self.xx[self.dim-1]=self.xx[self.dim-1]/self.A[self.dim-1,self.dim-1]
        for i in range(self.dim-2,-1,-1):
            for j in range(i+1,self.dim):
                self.xx[i]=self.xx[i]-self.A[i,j]*self.xx[j]
            self.xx[i]=self.xx[i]/self.A[i,i]
        return 0

    def gelim(self):
        if self.process == 1:
            print("the process of elimination\n")
        for k in range(self.dim):
            self.elim(k)
        self.back()


    def gcpelim(self):
        if self.process==1:
            print("the process of column principle elimination")
        for k in range(self.dim):
            pelement=math.fabs(self.A[k,k])
            i0=k
            for i in range(k,self.dim):
                if math.fabs(self.A[i,k])>pelement:
                    pelement=math.fabs(self.A[i,k])
                    i0=k
            if i0 !=k:
                for j in range(self.dim):
                    pelement=self.A[k,j]
                    self.A[k,j]=self.A[i0,j]
                    self.A[i0,j]=pelement
                pelement=self.xx[k]
                self.xx[k]=self.xx[i0]
                self.xx[i0]=pelement
            self.elim(k)
        self.back()

    def gapelim(self):
        if self.process==1:
            print("the process of all principle elimination")
        for k in range(self.dim):
            pelement=math.fabs(self.A[k,k])
            i0=k
            self.jk[k]=k
            for i in range(k,self.dim):
                for j in range(k,self.dim):
                    if math.fabs(self.A[i,j])>pelement:
                        pelement=math.fabs(self.A[i,j])
                        i0=i
                        self.jk[k]=j
            if i0 !=k:
                for j in range(self.dim):
                    pelement=self.A[k,j]
                    self.A[k,j]=self.A[i0,j]
                    self.A[i0,j]=pelement
                pelement=self.xx[k]
                self.xx[k]=self.xx[i0]
                self.xx[i0]=pelement
            i0=self.jk[k]
            if i0 !=k:
                for i in range(self.dim):
                    pelement=self.A[i,k]
                    self.A[i,k]=self.A[i,i0]
                    self.A[i,i0]=pelement
            self.elim(k)
        self.back()
        for k in range(self.dim-2,-1,-1):
            i0=self.jk[k]
            if i0 !=k:
                pelement=self.xx[k]
                self.xx[k]=self.xx[i0]
                self.xx[i0]=pelement
        return 0

if __name__=="__main__":
    a=elimination(5)
    a.A=np.array([[3.0,-2.0,5.3,-2.1,1.0],[1.0,4.0,-6.0,4.5,-6.0],[3.0,6.0,-7.3,-9.0,3.4],[-2.0,-3.0,1.0,-4.0,6.0],[1.0,-4.0,6.5,1.0,-3.0]])
    a.xx=np.array([28.3,-36.2,24.5,16.2,4.3])
    if a.gapelim()==1:
        print("no solution")
    else:
        print("gauss elimination method:\n")
        for i in range(a.dim):
            print(a.xx[i])
