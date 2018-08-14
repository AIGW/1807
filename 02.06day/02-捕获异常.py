#coding=utf-8
try:
	open('1.txt','r')
	#print(name)
	11/0
	print('laowang')
	print(1+1)
except (FileNotFoundError,NameError):
	print('报错了')
except Exception as ret:
	print('报错了',ret)
else:
	print('没有错误的执行')
finally:
	print('不管有没有错都执行')





try:
	age = int(input('请输入年龄'))
except ValueError:
	print('输入有误')

age = input('请输入年龄')
if age.isdigit():
	age = int(age)

else:
	print('输入有误')

