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
# gh = Gospers_Hack(2)
# print 'first:',gh.first
# print 'last:',gh.last
# for S in Gospers_Hack(2):
#     print S
	


