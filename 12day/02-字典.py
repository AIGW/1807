l = []
for i in range(3):
	d = {}
	name = input("请输入姓名")
	age = input("请输入年龄")
	sex = input("请输入性别")

	d["name"] = name
	d["age"] = age
	d["sex"] = sex
	l.append(d)
print(l)

for i in l:
	for j in i:
		print(i[j])

'''
	add = {"name":"name","age":"age","sex":"sex"}
	l.append(add)
for i in l:
	
	print(i)

'''
