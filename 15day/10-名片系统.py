list = [] 
	
def add(): #添加
	mp = {}
	name = input("请输入姓名:")
	age = int(input("请输入年龄:"))
	phone = int(input("请输入电话:"))
	mp["name"] = name
	mp["age"] = age
	mp["phone"] = phone
	list.append(mp)
	print("添加成功")


def find(): #查找
	name = input("请输入要查找的名字:")
	for mp in list:
		if mp["name"] == name:
			print("姓名:%s\n年龄:%d\n性别:%d"%(mp["name"],mp["age"],mp["phone"]))
			break


def change(): #修改
	name = input("请输入要修改的名字:")
	for mp in list:
		if mp["name"] == name:
			print("1、修改名字")
			print("2、修改年龄")
			print("3、修改电话")
			num = int(input("请选择功能:"))
			if num == 1:
				name = input("请输入新的名字:")
				mp["name"] = name
			elif num == 2:
				age = int(input("请输入新的年龄:"))
				mp["age"] = age
			elif num == 3:
				phone = int(input("请输入新的电话:"))
				mp["phone"] = phone
			break


def delete(): #删除
	name = input("请选择要删除的名字:")
	for mp in list:
		if mp["name"] == name:
			list.remove(mp)
			print("删除成功")
			break

def print_list():
	print("姓名        年龄        电话")
	for mp in list:
		print("%s        %d          %d"%(mp["name"],mp["age"],mp["phone"]))

def print_menu():
	print("欢迎进入名片管理系统".center(45,"*"))
	while True:
		print("1、添加人员名片")
		print("2、查找人员名片")
		print("3、修改人员名片")
		print("4、删除人员名片")
		print("5、打印人员名片")
		print("6、退出名片管理系统")
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
		print("谢谢使用，欢迎下次光临".center(45,"*"))
		exit()
print_menu()
