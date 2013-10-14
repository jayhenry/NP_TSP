# -*- coding:utf-8 -*-
import sys
from iter_gen import Gospers_Hack, Cindex,combi

print 'Hello, let\'s start.'
f = open('tsp.txt')
n = int(f.readline().split()[0])
print '# vertices:', n
# 读入所有点(x,y)到一个列表V，其元素是元组(x,y)
V = []
for line in f:
    coordinate = [float(x) for x in line.split() ]
    V.append(tuple(coordinate) )
# 建立顶点列表V的反向词典Vi,key是某个点(x,y)，value是这个点在V中的索引值index
Vi = {}
for i in range(len(V)):
    Vi[V[i]] = i
print 'Data read.'
# 计算所有顶点之间的距离，即边权值，到一个二维数组C。C[i][j]=Vi到Vj的距离
print 'Compute edge cost...'
C = [[0 for j in range(n)] for i in range(n) ]
for i in range(n):
    for j in range(n):
	C[i][j] = pow( pow( V[i][0]-V[j][0], 2)+pow( V[i][1]-V[j][1], 2), 0.5)

print 'Base case...'
nSS = pow(2,n-1) #用一个n=25bit的整形数S代表顶点集V的子集合S，所以子集合S构成的集合SS的元素数为2^(n-1)
# A是循环时所用的上一次的(子集S,终点i)对应最短路径的字典。这里S长度为m-1.
# B是该次循环计算得到的新的(S,i)->最短路径的字典。这里S长度为m.
# # A初始化长度为1的子集
# for S in Gospers_Hack(1,24):
#     A[Cindex(S,1,24)] = [float("+inf") for j in range(n) ]
# A[0][0] = 0.0
B = []
print 'Recurrence...'
# 第一层遍历子集的长度，从2到n
for m in range(2,n+1):
    # 第二层遍历m长度所有的子集，从0B0..01..1(m个1,25-m个0)到(0B1..10..0)
    B = [[] for i in range(combi(24,m-1))]
    for S in Gospers_Hack(m-1,24):
	B[Cindex(S,m-1,24)] = [0.0 for i in range(n)]
	# 第三层遍历所有终点:1...n-1
	for i in range(1,n):
	    # 最优子结构：由m-1长度S计算m长度S对应的最短周游路径
	    if m > 2:
	        minV = float("+inf")
	        for k in range(1,n):
	    	    if S&(1<<(k-1)) != 0 and k != i: # 遍历S去掉某个顶点的子集
	                S_ = S ^ (1<<(k-1))
	    	        minV =  min( minV, A[Cindex(S_,m-2,24)][k]+C[k][i] )
	    else :
		#minV = min( minV, A[Cindex(S_,1,24)][k]+C[k][i])
		minV = C[0][i]
	    B[Cindex(S,m-1,24)][i] = minV
    A = B
    B = []
print 'Solution to the original problem...'
S = pow(2,n-1) - 1
# minV = min j=1->n-1 { A[S][j] + C[j][0] }
minV = float("+inf")
for j in range(1,n):
    minV = min(minV, A[S][j]+C[j][0])
print 'minimum cost of travelling tour is', minV

