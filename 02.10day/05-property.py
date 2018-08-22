class Dog():
	def __init__(self):
		self.__age = 100

	def getAge(self):
		return self.__age

	def setAge(self,age):
		self.__age = age

	age = property(getAge,setAge)

dog = Dog()
#dog.setAge(150)
#print(dog.getAge())
dog.age = 900 #相当于写14行
print(dog.age)#相当于写15行
print(dog.getAge())