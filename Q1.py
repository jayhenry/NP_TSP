# -*- coding:utf-8 -*-
import sys
from iter_gen import Gospers_Hack, Cindex,combi

print 'Hello, let\'s start.'
f = open('test1.txt')
n = int(f.readline().split()[0])
print '# vertices:', n
# 读入所有点(x,y)到一个列表V，其元素是元组(x,y)
print 'Data read...'
V = []
for line in f:
    coordinate = [float(x) for x in line.split() ]
    V.append(tuple(coordinate) )
# 计算所有顶点之间的距离，即边权值，到一个二维数组C。C[i][j]=Vi到Vj的距离
print 'Compute edge cost...'
C = [[0 for j in range(n)] for i in range(n) ]
for i in range(n):
    for j in range(n):
	C[i][j] = pow( pow( V[i][0]-V[j][0], 2)+pow( V[i][1]-V[j][1], 2), 0.5)

# 用一个n=25bit的整形数S代表顶点集V的子集合S，所以子集合S构成的集合SS的元素数为2^(n-1)
# A是循环时所用的上一次的(S,i)->最短路径的字典。这里S为经过的点集，长度为m-1,i为终点.
# B是该次循环计算得到的新的(S,i)->最短路径的字典。这里S长度为m.
print 'Recurrence...'
# 第一层遍历子集的长度，从2到n
for m in range(2,n+1):
    # 第二层遍历m长度所有的子集，从0B0..01..1(m个1,25-m个0)到(0B1..10..0)
    print 'm:',m
    B = [[] for i in range(combi(n-1,m-1))]
    for S in Gospers_Hack(m-1,n-1):
	B[Cindex(S,m-1,n-1)] = [float("+inf") for i in range(n)]
	# 第三层遍历所有*在S集合中*的终点:1...n-1
	for i in range(1,n):
	    if S&(1<<(i-1)) != 0 :
	    # 最优子结构：由m-1长度S计算m长度S对应的最短周游路径
	        if m > 2:
	            minV = float("+inf")
	            for k in range(1,n):
	        	    if S&(1<<(k-1)) != 0 and k != i: # 遍历S去掉某个顶点的子集
	                        S_ = S ^ (1<<(i-1))
	        	        minV =  min( minV, A[Cindex(S_,m-2,n-1)][k]+C[k][i] )
	        else :
	            minV = C[0][i]
	        B[Cindex(S,m-1,n-1)][i] = minV
    A = B
    B = []
print 'Solution to the original problem...'
S = pow(2,n-1) - 1
# minV = min j=1->n-1 { A[S][j] + C[j][0] }
minV = float("+inf")
for j in range(1,n):
    x = A[Cindex(S,n-1,n-1)][j]
    y = C[j][0]
    minV = min(minV, A[Cindex(S,n-1,n-1)][j]+C[j][0])
print 'minimum cost of travelling tour is', minV

