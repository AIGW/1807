def w1(fun):
	def inner(*args,**kwargs):
		print('检查登录')
		fun(*args,**kwargs)
	return inner


@w1 #相当于pay = w1(pay)
def pay(*args,**kwargs):
	print('支付中')
	print(args)
	print(kwargs)

pay('哈哈'，'嘿嘿') #装饰完毕