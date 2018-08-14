class Dog():
	def __init__(self):
		self.__age = 0 #私有方法

	def sleep(self):
		print('sleep')

	def setAge(self,age):
		if age > 15 or age < 1:
			print("年龄不符合")
		else:
			self.__age = age
	
	def getAge(self):

		return self.__age

hsq = Dog()
hsq.setAge(10)
print(hsq.getAge())
