import random
while True:
	player = int(input("请出拳1、石头 2、剪刀 3、布:"))
	pc = random.randint(1,3)
	if player < 4 and player > 0:
		if(player==1 and pc==2) or (player==2 and pc==3) or (player==3 and pc==1):
			print("玩家赢")
		elif player == pc:
			print("平局")

		else:
			print("电脑赢")
	else:
		print("不合法")
