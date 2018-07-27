list = []
def add():
	for i in range(3):
		l = []
		for j in range(3):
			grade = float(input("请输入成绩"))
			l.append(grade)
		list.append(l)
	print(list)


maxgrade = 0 #记录最大值
mp = 0  #记录最大值的索引
def mmax():
	global maxgrade
	global mp
	for p,i in enumerate(list):
		if sum(i) > maxgrade:
			maxgrade = sum(i)
			mp = p
	print(maxgrade)
	print(mp)
	print("平均分是%.02f"%(maxgrade/3))
	print(list[mp][0],list[mp][1],list[mp][2])
add()
mmax()
