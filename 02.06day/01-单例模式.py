
class Dog():
	__instance = None

	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
		

dog1 = Dog()
print(id(dog1))
dog2 = Dog()
print(id(dog2))
dog3 = Dog()
print(id(dog3))










class Son():
	__instance = None
	__flag = False
	def __init__(self,name):
		if Son.__flag == False:
			self.name = name
			Son.__flag = True

	def __new__(cls,*args,**kwargs):#重写
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

xifu = Son('小红')
print(id(xifu))

xifu1 = Son('小花')
print(id(xifu1))

print(xifu.name) 
print(xifu1.name)















class Dog():
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
dog1 = Dog()
print(id(dog1))
dog2 = Dog()
print(id(dog2))
dog3 = Dog()
print(id(dog3))
dog4 = Dog()
print(id(dog4))
