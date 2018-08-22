def w1(fun):
	def inner():
		print('检查登录')
		return fun()
	return inner

@w1 
def pay():
	print('支付中')
	return '老王'

ret = pay() #此时装饰器已经装饰完毕
print(ret)