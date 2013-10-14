# -*- coding:utf-8 -*-
class Gospers_Hack:
    def __init__(self, m, n ):
	self.m = m # ������
	self.first = pow(2, m ) - 1
	self.last = pow(2, n ) - pow(2, n-m )
    def __iter__(self):
	self.x = self.first
	return self
    def next(self):
	xr = self.x
	if (xr > self.last ):
	    raise StopIteration
	x = self.x
        s = x & (-x) # �ҵ����ұ�1��λ��
        r = s + x # �ҵ����ұ�����1(k��)���յ�λ��+1��������λ����1
        x = r | (((x ^ r) >> 2) // s) # ��(k-1)������1�ŵ�β��
	self.x = x
	return xr
def combi(n,k):
    if n < k:
	return 0
    else :
        denominator = 1
	numerator = 1
	for i in range(1,k+1):
	    denominator *= i
	    numerator *= (n-i+1)
	return numerator/denominator
def Cindex(x,k,m):
    C = [0 for i in range(k+1)]
    count = 1
    for i in range(m):
	if  (x >> i) & 1  :
	    C[count] = i
	    count += 1
    index = 0
    for i in range(1,k+1):
	index += combi(C[i],i)
    return index

# # test    
# gh = Gospers_Hack(2-1,24)
# print 'first:',gh.first
# print 'last:',gh.last
# count = 0
# for S in Gospers_Hack(2-1,24):
#     print count,":",S,
#     print "Cindex:",Cindex(S,1,24)
#     count += 1

	


