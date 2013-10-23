# -*- coding:utf-8 -*-
import sys
from iter_gen import Gospers_Hack, Cindex,combi

print 'Hello, let\'s start.'
f = open('test1.txt')
n = int(f.readline().split()[0])
print '# vertices:', n
# �������е�(x,y)��һ���б�V����Ԫ����Ԫ��(x,y)
print 'Data read...'
V = []
for line in f:
    coordinate = [float(x) for x in line.split() ]
    V.append(tuple(coordinate) )
# �������ж���֮��ľ��룬����Ȩֵ����һ����ά����C��C[i][j]=Vi��Vj�ľ���
print 'Compute edge cost...'
C = [[0 for j in range(n)] for i in range(n) ]
for i in range(n):
    for j in range(n):
	C[i][j] = pow( pow( V[i][0]-V[j][0], 2)+pow( V[i][1]-V[j][1], 2), 0.5)

# ��һ��n=25bit��������S�����㼯V���Ӽ���S�������Ӽ���S���ɵļ���SS��Ԫ����Ϊ2^(n-1)
# A��ѭ��ʱ���õ���һ�ε�(S,i)->���·�����ֵ䡣����SΪ�����ĵ㼯������Ϊm-1,iΪ�յ�.
# B�Ǹô�ѭ������õ����µ�(S,i)->���·�����ֵ䡣����S����Ϊm.
print 'Recurrence...'
# ��һ������Ӽ��ĳ��ȣ���2��n
for m in range(2,n+1):
    # �ڶ������m�������е��Ӽ�����0B0..01..1(m��1,25-m��0)��(0B1..10..0)
    print 'm:',m
    B = [[] for i in range(combi(n-1,m-1))]
    for S in Gospers_Hack(m-1,n-1):
	B[Cindex(S,m-1,n-1)] = [float("+inf") for i in range(n)]
	# �������������*��S������*���յ�:1...n-1
	for i in range(1,n):
	    if S&(1<<(i-1)) != 0 :
	    # �����ӽṹ����m-1����S����m����S��Ӧ���������·��
	        if m > 2:
	            minV = float("+inf")
	            for k in range(1,n):
	        	    if S&(1<<(k-1)) != 0 and k != i: # ����Sȥ��ĳ��������Ӽ�
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

