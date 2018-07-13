account = "123456"
password = "abc"
act = input("请输入账号")
pwd = input("请输入密码")
if act == account and pwd == password:
	print("登录成功")
elif act!= account:
	print("账号不对")
elif pwd!= password:
	print("密码不对")

