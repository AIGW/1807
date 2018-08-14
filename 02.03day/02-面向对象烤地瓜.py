
class DiGua():
	def __init__(self):
		self.status = "生的"
		self.times = 0
		self.z = []
	def __str__(self):
		msg = '我烤的地瓜成熟度%s'%self.status
		return msg+str(self.z)
		
	def cook(self,time):
		times+=time
		if self.times >= 1 and self.times <= 2:
			self.status = '生的'
		elif self.times >= 3 and self.times <= 5:
			self.status = '半生不熟'
		elif self.times >= 6 and self.times <= 8:
			self.status = '8分熟'
		elif self.times >= 9 and self.times <= 12:
			self.status = '正好'
		elif self.times > 12:
			self.status = '烤成炭了'
	def addcondiments(self,name):
		self.dg.append(dg)

list = ['番茄酱','孜然','辣椒','甜面酱']
kaodigua = DiGua()

for i in range(5):
	kaodigua.cook(random.randint(1,4))
	z = random.choice(list)
	kaodigua.addz(z)
	list.remove(z)
	print(kaodigua)


