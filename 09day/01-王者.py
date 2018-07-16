account = "laoguo"
password = "123456"

i = 0
while True:
	while i < 3:


		iacc = input("请输入账号")
		ipwd = input("请输入密码")

		if account == iacc and password == ipwd:
			print("登录成功")
		rum = input("请选择英雄")
		if num == 0:
			print("鲁班")
		elif num == 1:
			print("妲己")
		elif unm == 2:
			print("程咬金")
		elif num == 3:
			print("阿珂")
else:
	i+=1
	print("登录失败%d次"%i)
