# -*- coding:utf-8 -*-
import sys

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
nS = pow(2,n-1) 
A = [[float("+inf") for j in range(n) ] for i in range(n)]
A[0][0] = 0.0
B = [[]]
# print 'Recurrence...'
# for m in range(2,n+1):
#     for S in some set:
# 	for i in range(1,n):
# 	    A[S][i] = min k-0-i { A[S-set([k])][k] + C[k][i] }
# print 'Solution to the original problem...'
# minV = min j_1->n-1 { A[set(range(n))][j] + C[j][0] }
# print 'minimum cost of travelling tour is', minV
