# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:06:54 2019

@author: Administrator
"""
import numpy as np
from numpy.linalg import inv
#构建矩阵
x=np.array([[1005,1],[2100,1],[3950,1],[9100,1],[15800,1]])
c=np.array([0.1,0.2,0.4,0.8,1.6])
#由于构建的c是行向量，需要转置，c.T用来转置
c2=c.T
#inv函数求逆，np.dot是乘法
x2=inv(np.dot(x.T,x))
x3=np.dot(x2,x.T)
#计算回归系数
B=np.dot(x3,c2)
#构建测试数据矩阵，用来测试
xtest=np.array([[3005,1],[3100,1],[2985,1]])
#测试
C=np.dot(xtest,B)
#求预测值的均值
Cmean=np.mean(C)
print("回归系数",B,"预测值",C,"均值",Cmean)
X=np.dot(c,B)

from pylab import plot, xlabel, ylabel, legend
plot(c, x[:,0], 'bo',label='R2')
plot(c,X[:,0])
xlabel('c')
ylabel('H')
legend(loc='upper left')
