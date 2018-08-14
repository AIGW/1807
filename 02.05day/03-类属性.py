class Dog():
	print('哈哈哈哈哈哈')
	count = 10
	def __init__(self,name):
		self.name = name#实例属性
		self.__age = 10


	def getAge(self):
		return self.__age








print(Dog.count)#通过类访问类属性
