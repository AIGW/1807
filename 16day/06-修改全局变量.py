
a = 100
#在函数内部  想修改全局变量

def test():
	global a
	a = 1000
	print(a)

test()
print(a)
