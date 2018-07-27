
def clum(x,y,z):
	if z == "+":
		c = x+y
	elif z == "-":
		c = x-y


	return c
'''
ret = clum(1,2,"-")
print(ret)
'''


def clum1(x,y,z):
	#print(z)#打印匿名函数地址
	ret = z(x,y)
	return ret

#ret = clum1(1,2,lambda x,y:x+y)
#print(ret)
#print(clum1)#打印函数地址
ret = clum1(1,2,lambda x,y:x-y)
print(ret)

