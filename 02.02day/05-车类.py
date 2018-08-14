class car():
	def__init__(self,name,type):

		self.name = name
		self.type = type

	def color(self):
		print("白色")
	def move(self):
		print("车在跑")
	def __str__(self):
		msg = "车辆颜色是"
	def introduce(self):
		print("车名是%s,型号为%s"%(self.name,self.type))


yueye = car("路虎"，3)
yueye.color()
yueye.move()
print("车的型号为:%S"%yueye.xinghao)
print("车的颜色为:%s"%yueye.color)
	
