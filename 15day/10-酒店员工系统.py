list = [] 
	
def add():
	sta = {}
	name = input("请输入员工姓名:")
	age = int(input("请输入员工年龄:"))
	sta["name"] = name
	sta["age"] = age
	list.append(sta)
	print("添加成功")


def find():
	name = input("请输入要查找的名字:")
	for sta in list:
		if sta["name"] == name:
			print("员工姓名:%s\n员工年龄:%d"%(sta["name"],sta["age"]))
			break


def change():
	name = input("请输入要修改的名字:")
	for sta in list:
		if sta["name"] == name:
			print("1、修改名字")
			print("2、修改年龄")
			num = int(input("请选择功能:"))
			if num == 1:
				name = input("请输入新的名字:")
				sta["name"] = name
			elif num == 2:
				age = int(input("请输入新的年龄:"))
				sta["age"] = age
			break


def delete():
	name = input("请选择要删除的名字:")
	for sta in list:
		if sta["name"] == name:
			list.remove(sta)
			print("删除成功")
			break

def print_list():
	print("姓名			年龄")
	for sta in list:
		print("%s		 %d"%(sta["name"],sta["age"]))

def print_menu():
	print("欢迎来到酒店员工管理系统".center(30," "))
	while True:
		print("1、添加员工信息")
		print("2、查找员工信息")
		print("3、修改员工信息")
		print("4、删除员工信息")
		print("5、打印员工信息")
		print("6、退出酒店系统")
		input_info()

def input_info():
	num = int(input("请选择功能:"))
	if num == 1:
		add()
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num == 6:
		print("谢谢使用，欢迎下次光临".center(30," "))
		exit()
print_menu()
