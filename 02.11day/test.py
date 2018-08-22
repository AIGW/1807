def fib():
	a,b = 0,1
	print('--------1--------')
	for i in range(10):
		print('----------2-----------')
		#print(b)
		temp = yield b
		print(temp)
		print('-----------------3------------------')
		a,b = b,a+b
	#print(fib())
	#G = fib()
	#print(next(G))
		#print(i)
	#print(G.__next__())
	#print(G.__next__())