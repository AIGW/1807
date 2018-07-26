list = []  #装员工
code = 1000

def showError(msg):#显示错误
	print("输入有误,请重新输入"+msg)

def isNum(num):    #判断是否一个数字
	if num.isdigit():
		return True
	else:
		return False


def add(): #添加功能
	st = {}
	while True:
		name = input("请输入员工姓名:")
		if len(name) >= 2 and len(name) <= 4:	
			st["name"] = name
			break
		else:
			showError("员工名字必须大于2小于4")
	while True:
		age = input("请输入员工年龄:")
		if isNum(age):
			age = int(age)
		else:
			print("输入有误")
			continue
		if age > 1 and age < 120:
			st["age"] = age
			break
		else:
			showError("年龄必须大于1小于120")
	if len(list) == 0:
		st["code"] = code
	else:
		st["code"] = list[len(list)-1]["code"]+1
	st["isdelete"] = False
	list.append(st)
	print("添加成功")


	

def find():    #查找功能
	
	name = input("请输入要查找的员工姓名:")
	for st in list:
		if st["name"] == name:
			print("\n姓名为:%s\n年龄为:%d"%(st["name"],st["age"]))
			break

def change():  #修改功能
	
	name = input("请输入员工姓名:")
	flag =False   #假设这里面没有这个
	for st in list:
		if st["name"] == name:
			flag = True #找到以后改成True
			while True:
				print("员工姓名:%s\n员工年龄:%d"%(st["name"],st["age"]))

				print("1、修改姓名:")
				print("2、修改年龄:")

				num = input("请选择功能:")
				if isNum(num):
					num = int(num)
				else:
					print("输入有误")
					continue
				if num == 1:
					name = input("请输入新的名字:")
					st["name"] = name
				elif num == 2:
					age = int(input("请输入新的年龄:"))
					st["age"] = age
				break
			break
	if not flag:
				
			print("查无此人")
			

def delete():  #删除功能
	name = input("请选择要删除的员工姓名:")
	dellist = []
	for st in list:
		if st["name"] == name:
			#list.remove(st)
			dellist.append(st)
			#print("删除成功")
			#break
	if dellist:
		print("序号        姓名        年龄        工号")
		for p,st in enumerate(dellist):
			print("%d        %s        %d        %d"%((p+1),st["name"],st["age"],st["code"]))
		num = input("请删除序号")
		if isNum(num):
			num = int(num)
			list[list.index(dellist[num-1])]["isdelete"] = True
			print("删除成功")

def print_list():  #打印全部
	print("姓名        年龄        工号")
	for st in list:
		if st["isdelete"] == False:

			print("%s        %d        %d"%(st["name"],st["age"],st["code"]))

def print_menu():
	print("欢迎进入酒店管理系统".center(30," "))
	while True:
		print("1、添加员工信息")
		print("2、查找员工信息")
		print("3、修改员工信息")
		print("4、删除员工信息")
		print("5、打印员工信息")
		print("6、退出管理系统")
		input_info()  #调用选择功能函数

def input_info():
	num = input("请选择功能:")
	if isNum(num):
		num = int(num)
	else:
		print("输入有误")

	if num == 1:
		add()  #调用添加函数
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num == 6:
		print("谢谢使用，欢迎再来".center(30," "))
		exit()
				
			
		
print_menu()
