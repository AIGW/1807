s = []
while True:

		print("*********************欢迎来到学生管理系统******************")
		print("1:添加学生信息")
		print("2:查找学生信息")
		print("3:修改学生信息")
		print("4:删除学生信息")
		print("5:退出学生系统")


		num = int(input("请选择功能:"))
		if num == 1:
			sd = {}
			name = input("请输入姓名:")
			age = int(input("请输入年龄:"))
			sex = input("请输入性别:")
			phone = int(input("请输入电话:"))
			mz = input("请输入民族:")
			
			sd["name"] = name
			sd["age"] = age
			sd["sex"] = sex
			sd["phone"] = phone
			sd["mz"] = mz
			s.append(sd)
			print(s)
		elif num == 2:
			name = input("请输入学生名字:")
			for sd in s:
				if sd["name"] == name:
					print("学生名字:%s\n学生年龄:%d\n学生性别:%s\n学生电话:%d\n学生民族:%s"%(sd["name"],sd["age"],sd["sex"],sd["phone"],sd["mz"]))
					break
			
		elif num == 3:
				name = input("请输入学生名字:")
				for sd in s:
					if sd["name"] == name:
						print("学生名字:%s\n学生年龄:%d\n学生性别:%s\n学生电话:%d\学生民族:%s"%(sd["name"],sd["age"],sd["sex"],sd["phone"],sd["mz"]))
						print("1:修改名字:")
						print("2:修改年龄:")
						print("3:修改性别")
						print("4:修改电话")
						print("5:修改民族")
						num = int(input("请选择修改序号:"))
						if num == 1:
							name = input("请输入新的名字:")
							sd["name"] = name
						elif num == 2:
							age = int(input("请输入新的年龄:"))
							sd["age"] = age
						elif num == 3:
							sex = input("请输入新的性别:")
							sd["sex"] = sex
						elif num == 4:
							phone = int(input("请输入新的电话:"))
							sd["phone"] = phone
						elif num == 5:
							mz = input("请输入新的民族:")
							sd["mz"] = mz

						print("修改成功")
		elif num == 4:
			name = input("请输入学生姓名:")
			for sd in s:
				if sd["name"] == name:
					s.remove(sd)
				
					print("删除成功")
					break
		elif num == 5:

			print("******************谢谢使用，欢迎下次再来***************")
			break
