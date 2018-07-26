def test(a,b,c):
	c = a+b+c
	print(c)

  #test(1,2,3)


 #不定长参数的写法
def test(a,*args,b=12,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
	sum = 0
	sum = sum+a
	for i in args:
		sum = sum+i
	sum = sum+b
	for v in kwargs.values():
		sum = sum+v
	return sum

ad = test(1,2,3,4,5,b=20,m=12,n=22)
print(ad)
	
