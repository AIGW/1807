class Father():
	def __init__(self,name):
		self.name = name
		self.__sfq = 100

	def __play(self):
		print('打麻将')

	def getsfq(self):#共有方法
		return self.__sfq

	def Play(self):#共有方法
		self.__play()

class Son(Father):
	pass


son = Son('宙斯')

print(son.name)
print(son.getsfq())
son.Play()
