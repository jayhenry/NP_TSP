# -*- coding:utf-8 -*-
import sys
from iter_gen import Gospers_Hack
print 'Hello, let\'s start.'
f = open('tsp.txt')
n = int(f.readline().split()[0])
print '# vertices:', n
V = []
for line in f:
    coordinate = [float(x) for x in line.split() ]
    V.append(tuple(coordinate) )
Vi = {}
for i in range(len(V)):
    Vi[V[i]] = i
print 'Data read.'

print 'Compute edge cost...'
C = [[0 for j in range(n)] for i in range(n) ]
for i in range(n):
    for j in range(n):
	C[i][j] = pow( pow( V[i][0]-V[j][0], 2)+pow( V[i][1]-V[j][1], 2), 0.5)

m = 2
# S = set()
i = 0
A = [[]]

print 'Base case...'
# SS = []
# for i in range(pow(2,n-1)):
#     S = set([0])
#     vi = 1
#     while i > 0:
# 	if i%2 == 1:
# 	    S.add(vi)
# 	i >>= 1
# 	vi += 1
#     S = frozenset(S)
#     SS.append(S)
# print 'size of SS:', len(SS)
# SSi = {}
# for i in range(len(SS)):
#     SSi[SS[i]] = i
nSS = pow(2,n-1) #用一个25bit的整形数S代表各顶点的子集合S，所以子集合构成的集合SS的元素数为2^(n-1)
# A = [[float("+inf") for j in range(n) ] for i in range(n)]
A = {}
for i in range(n):
    A[i] = [float("+inf") for j in range(n) ]
A[0][0] = 0.0
B = {}
print 'Recurrence...'
for m in range(2,n+1):
    B = {}
    for S in Gospers_Hack(m):
	B[S] = [0.0 for i in range(n)]
	for i in range(1,n):
	    minV = float("+inf")
	    for k in range(1,n):
		if S&(1<<(k-1)) != 0 and k != i: # 遍历S去掉某个顶点的子集
	            S_ = S ^ (1<<(k-1))
		    minV =  min( minV, A[S_][k]+C[k][i] )
	    B[S][i] = minV
    A = B
print 'Solution to the original problem...'
S = pow(2,n-1) - 1
# minV = min j=1->n-1 { A[S][j] + C[j][0] }
minV = float("+inf")
for j in range(1,n):
    minV = min(minV, A[S][j]+C[j][0])
print 'minimum cost of travelling tour is', minV
