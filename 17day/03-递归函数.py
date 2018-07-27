
#阶乘
#5!=5*4*3*2*1
#4!=4*3*2*1
#3!=3*2*1

i = 1
ret = 1
while i <= 5:
	ret*=i #ret = ret*i
	i+=1
print(ret)


#5!=5*4!
#4!=4*3!
#3!=3*2!
#2!=2*1

def xxxx(d):
	d *1
def xxx(c):
	c*xxxx(c-1)

def xx(a):
	#4*3!
	a*xxx(a-1)
	#return"老郭"

'''
5*4*3*2*1

4*test(4-1)
3*test(3-1)
2*test(2-1)
'''

def test(num):
	if num == 1:
		return num
	else:
		return num*test(num-1)
	#5*"老郭"
	#5*4*3!
#def test2(num):
	#return num *test2(num-1)
#test2(10)

ret = test(5)
print(ret)

