list = []
while True:
	print("欢迎来到学生管理系统")
	print("1:添加学生信息")
	print("2:查找学生信息")
	print("3:修改学生系统")
	print("4:删除学生信息")
	print("5:谢谢使用，再见")

	num = int(input("请选择功能:"))
	if num == 1:
		ls = {}
		name = input("请输入名字:")
		age = int(input("请输入年龄:"))
		sex = input("请输入性别:")
		mz = input("请输入民族:")
		contact = int(input("请输入联系方式:"))
		ls["name"] = name
		ls["age"]
