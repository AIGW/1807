x = float(input("请输入x值:"))
y = float(input("请输入y值:"))
z = input("请输入+-*/:")


if z == "+":
	print("x+y的值%d"%(x+y))
elif z == "-":
	print(x-y)
elif z == "*":
	print(x*y)
elif z == "/":
	if y == 0:
		print("不合法")
	print(x/y)
'''
#xuan = float(input("请输入"))
x = float(input("请输入数字"))
y = float(input("请输入"))
a = x+y 
print(a)
b = x-y
print(b)
'''
c = x*y
print(c)
d = x/y
print(d)

