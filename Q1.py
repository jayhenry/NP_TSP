# -*- coding:utf-8 -*-
import sys
from iter_gen import Gospers_Hack, Cindex,combi

print 'Hello, let\'s start.'
f = open('tsp.txt')
n = int(f.readline().split()[0])
print '# vertices:', n
# �������е�(x,y)��һ���б�V����Ԫ����Ԫ��(x,y)
V = []
for line in f:
    coordinate = [float(x) for x in line.split() ]
    V.append(tuple(coordinate) )
# ���������б�V�ķ���ʵ�Vi,key��ĳ����(x,y)��value���������V�е�����ֵindex
Vi = {}
for i in range(len(V)):
    Vi[V[i]] = i
print 'Data read.'
# �������ж���֮��ľ��룬����Ȩֵ����һ����ά����C��C[i][j]=Vi��Vj�ľ���
print 'Compute edge cost...'
C = [[0 for j in range(n)] for i in range(n) ]
for i in range(n):
    for j in range(n):
	C[i][j] = pow( pow( V[i][0]-V[j][0], 2)+pow( V[i][1]-V[j][1], 2), 0.5)

print 'Base case...'
nSS = pow(2,n-1) #��һ��n=25bit��������S�����㼯V���Ӽ���S�������Ӽ���S���ɵļ���SS��Ԫ����Ϊ2^(n-1)
# A��ѭ��ʱ���õ���һ�ε�(�Ӽ�S,�յ�i)��Ӧ���·�����ֵ䡣����S����Ϊm-1.
# B�Ǹô�ѭ������õ����µ�(S,i)->���·�����ֵ䡣����S����Ϊm.
# # A��ʼ������Ϊ1���Ӽ�
# for S in Gospers_Hack(1,24):
#     A[Cindex(S,1,24)] = [float("+inf") for j in range(n) ]
# A[0][0] = 0.0
B = []
print 'Recurrence...'
# ��һ������Ӽ��ĳ��ȣ���2��n
for m in range(2,n+1):
    # �ڶ������m�������е��Ӽ�����0B0..01..1(m��1,25-m��0)��(0B1..10..0)
    B = [[] for i in range(combi(24,m-1))]
    for S in Gospers_Hack(m-1,24):
	B[Cindex(S,m-1,24)] = [0.0 for i in range(n)]
	# ��������������յ�:1...n-1
	for i in range(1,n):
	    # �����ӽṹ����m-1����S����m����S��Ӧ���������·��
	    if m > 2:
	        minV = float("+inf")
	        for k in range(1,n):
	    	    if S&(1<<(k-1)) != 0 and k != i: # ����Sȥ��ĳ��������Ӽ�
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

