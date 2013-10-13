# -*- coding:utf-8 -*-
class Gospers_Hack:
    def __init__(self, m, n ):
	self.m = m # 比特数
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
        s = x & (-x) # 找到最右边1的位置
        r = s + x # 找到最右边连续1(k个)的终点位置+1，并将此位置置1
        x = r | (((x ^ r) >> 2) // s) # 将(k-1)个连续1放到尾部
	self.x = x
	return xr
# gh = Gospers_Hack(2)
# print 'first:',gh.first
# print 'last:',gh.last
# for S in Gospers_Hack(2):
#     print S
	


