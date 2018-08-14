class Phone():
	
	count = 0
	def __init__(self,color):
		self.color = color
		Phone.count+=1
	def call(self):
		print('打电话')









xiaomi = Phone('白色')
xiaomi1 = Phone('黑色')
xiaomi2 = Phone('金色')

print(Phone.count)
