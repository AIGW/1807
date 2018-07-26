list = []
i = 2
for i in range(2,101):
	for j in range(2,i):
		if i % j == 0:
			list.append(i)
print(list)
