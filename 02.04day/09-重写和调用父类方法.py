class Dog():

	def __init__(self,name):
		self.name = name
		print('父类的')

	def wark(self):
		print('汪汪汪')


class hsq(Dog):
	def __init__(self,name):
		self.name = name
		print('子类')

	def wark(self):
		print('嗷嗷嗷')

class xtq(Dog):
	def wark(self):
		print('狂叫')
	


hsq1 = hsq('二哈')
hsq1.wark()


xtq1 = xtq('哮天犬')
xtq1.wark()
