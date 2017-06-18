l=[1,2,"a", [3,4,5], 6, "b"]

for x in l:
	print x,
	if type(x) is list:
		print 'list'
