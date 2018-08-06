mz = input("请输入备份文件名字(要有后缀名)")

f = open(mz,"r")
content = f.read()
position = mz.rfind(".")

newmz = name[:position]+"备份"+name[position:]

f1 = open(newmz,"w")
f1.write(content)
	

f.close()
f1.close()



