import random
class ChaShu():
	def caishuzi(self):
		pc = random.randint(1,30)
		for i in range(1,11):
			player = int(input("请输入数字"))
			if player > pc:
				print("猜大了")
			elif player < pc:
				print("猜小了")
			elif player == pc:
				print('猜对了')
				break

cs = ChaShu()
cs.caishuzi()
