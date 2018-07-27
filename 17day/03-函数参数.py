
def test(a,b,*args,c=12,**kwargs):
	print(a)
	print(b)
	print(args)
	print(c)
	print(kwargs)

t = (3,4,5) #拆包
d = {"m":7,"n":12}
test(1,2,*t,c=14,**d)
