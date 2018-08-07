class person:
	def run(self):
		print("老马在跑")
	def tiao(self):
		print("老马在跳")
	def zou(self):
		print("老马在走")
	def zuo(self):
		print("老马坐着")
	def introduce(self):
		print("我年龄是%d 我身高是%d"%(self.age,self.height))

laoma = person()
laoma.run()
laoma.tiao()
laoma.zou()
laoma.zuo()



laoma.age = 35
laoma.height = 175
laoma.introduce()

print(laoma.age)
print(laoma.height)


ln = person()
ln.run()
ln.tiao()
ln.zou()
ln.zuo()
ln.age = 32 #添加属性
ln.height = 168
ln.introduce()
