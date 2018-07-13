'''
1-----石头
2-----剪刀
3-----布

玩家: 1---2   2---3   3---4

电脑: 1
'''
'''
import random
'''
import random

while True:
	player = int(input("请输入1、石头 2、剪刀 3、布:"))
	pc = random.randint(1,3)#随机一个1-3之间的数字
	if player < 4 and player > 0:
		if(player==1 and pc==2) or (player==2 and pc==3) or (player==3 and pc==1):
			print("玩家赢")
		elif player == pc:
			print("平局")
		else:
			print("电脑赢")
	else:
		print("不合法")

