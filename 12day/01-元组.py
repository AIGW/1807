s = {"name":"郭维","sex":"男","mz":"汉","brithday":"1989年3月21日","address":"山西省文水县南安镇"}

#添加一对键值对
s["age"] = 29
print(s)
#s["name"] = "老郭"
#print(s)


#删除
#s.pop("name")
#print(s)

#查找
#print(s["sex"])


#改
s["name"] = "郭维维"

for i in s:
	print(i)
	print(s[i])



for i in s.keys():
	print(i)
	print(s[i])


for i in s.values():
	print(i)


for k,v in s.items():
	print(k)
	print(v)



for i in s.itmes():
	print(i)
	print(i[0])
	print(i[1])
