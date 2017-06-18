def sumall (l):
	return reduce (lambda x,y: x+y, l) 


mylist = [1,2,3,4,5,6,7]

print mylist
print sumall (mylist)



