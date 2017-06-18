def squareall (l):
	result = []
	return ( map (lambda x: x**2, l) )


mylist = [1,2,3,4]

sqlist = squareall (mylist)


print sqlist

sqlist.append(100)

print sqlist
print len(sqlist)


