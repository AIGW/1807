'''
def test(a):
	a+=a
	print(a) #[1,2,1,2]

x = [1,2]
test(x)
print(x)  #[1,2,1,2]

'''



def test1(a):
	a=a+a
	print(a) #[1,2,1,2]

x = [1,2]
test1(x)
print(x)  #[1,2]










def ad(num):
	if num == 1:
		return num
	else:
		return num*ad(num-1)

ret = ad(5)
print(ret)
