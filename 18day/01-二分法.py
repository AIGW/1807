
list = [1,2,4,5,7,9,11,13,15,16]#有序序列
min = 0 #最小索引
max = len(list)-1 #最大索引
count = 9 #找4的索引
while True:
	center = int((min+max)/2)
	if list[center] > count:
		max = center - 1
	elif list[center] < count:
		min = center + 1
	elif list[center] == 1:
		print("索引是%d"%center)
		break
