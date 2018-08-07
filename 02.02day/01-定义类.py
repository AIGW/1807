class car:
	#有行为的类
	def run(self):
		print("跑")
	def turn(self):
		print("转向")




bujiadi = car()#通过汽车类创建一个布加迪的对象
bujiadi.run()#目前不需要传参数
bujiadi.turn()#目前不需要传参数





class bingxiang():
	def opendoor(self):
		print("开门")
	def zhuangdaxiang(self):
		print("装大象")
	def closedoor(self):
		print("关门")

ximenzi = bingxiang()
ximenzi.opendoor()
ximenzi.zhuangdaxiang()
ximenzi.closedoor()
