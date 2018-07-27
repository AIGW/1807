

def clum(x,y,z):
	#print(z)打印匿名函数地址
	ret = z(x,y)
	return ret

ret = clum(1,2,lambda x,y:x+y)
print(ret)
#print(clum)#打印函数地址
#ret = clum(1,2,lambda x,y:x-y)
#print(ret)  




fun = lambda x,y:x+y
print(fun(1,2))




def test(x,y):
	return x+y

ret = test(1,2)
print(ret)
