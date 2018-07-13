h = float(input("请输入身高"))
m = float(input("请输入身价"))
y = float(input("请输入颜值分"))


if h > 180 and m > 1000000 and y > 99:
	print("高富帅")
elif m > 1000000 and y > 99:
	print("富帅")
elif y > 99:
	print("帅")
elif h < 160 and m < 100 and y < 60:
	print("矮矬穷")
