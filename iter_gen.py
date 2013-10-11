class Gospers_Hack:
    def __init__(self, m ):
	self.m = m
	self.first = pow(2, m-1 ) - 1
	self.last = pow(2, 24 ) - pow(2, 24-m+1 )
    def __iter__(self):
	self.x = self.first
	return self
    def next(self):
	xr = self.x
	if (xr > self.last ):
	    raise StopIteration
	x = self.x
        s = x & (-x)
        r = s + x
        x = r | (((x ^ r) >> 2) // s)
	self.x = x
	return xr
# gh = Gospers_Hack(2)
# print 'first:',gh.first
# print 'last:',gh.last
# for S in Gospers_Hack(2):
#     print S
	


