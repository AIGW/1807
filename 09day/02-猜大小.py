import random
i = 0 
num = random.randint(1,100)
while i < 9:
	u_num = int(input("请输入猜的数字"))
	if u_num > num:
		print("猜大了")
	elif u_num < num:
		print("猜小了")
	else:
		print("恭喜你猜对了")
		break
	i+=1
