import sys

a=sys.argv[1]
b=sys.argv[2]

if (a==b):
	print a,
	print b,
	print "are euql"
else: 
	if (a>b):
		print a, "is greater than", b
	else:
		print a, "is smaller than", a
