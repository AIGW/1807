list = [1,3,5,25,17,8,20,4,15,6,11]
#list.sort()升序
#list.sort(reverse=True)#降序
#list.reverse()#倒序
#print(list)


for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)
