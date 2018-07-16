'''
i = 1
while i <= 9:
	row = 1
	while row <= i:
		print("%d*%d=%d\t"%(row,i,row*i),end = "")
		row+=1
	print("")
	i+=1
'''


for i in range(1,10):
	for j in range(1,i+1):
		print("%d*%d=%d"%(j,i,j*i),end = "\t")
	print("")
