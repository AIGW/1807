
def test(a,b,c=12):
	print(a,b,c)


test(1,2,3)
test(a=1,b=2,c=15)
test(c=12,b=8,a=20)
test(1,b=12,c=15)
test(a=13,b=11,8) #不可以
test(a=14,17,6) #不可以
