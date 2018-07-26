
home = ["老王","老赵","老宋"]


home1 = ["老王"]

home1.append("老宋")#添加 
print(home1)


home1.append("老赵")
print(home1)
#home1.insert(0,"老宋")#插队
#print(home1)

#home1.pop()#删除
#print(home1)

#home1.pop(0)#谁在0号位 删谁
#print(home1)

home1.remove("老宋")#根据名字删除
print(home1)


#查找索引为0的值
print(home1[0])


#修改
home1[0] = "老李"
print(home1)



#特殊方法
#extend() 会把添加的元素拆开分别插入到列表 
#append() 把添加的元素当做一个元素插入到列表



#xxx.sort()升序
#xxx.sort(revese=True)降序
#xxx.reverse()倒序
