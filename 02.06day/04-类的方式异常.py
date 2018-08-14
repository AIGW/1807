class showError(Exception):
	def __init__(self,name):
		self.name = name
class InputManger():

	def my_input(self):
		name = input('请输入名字')
		try:
			if name == '老王':
				raise ShowError(self.name)
		except ShowError as ret:
			print('输入%s就报错'%ret.name)
im = InputManger()
im.my_input()
		
'''

if len(name) < 5:
	raise showError(len(name))
except showError as ret:
	print('至少需要%d位，传的值是%d'%(ret,leastLen,ret.len))

'''
