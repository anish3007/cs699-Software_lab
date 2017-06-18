import math, sys

def func (x,y): 
	p= x*x 
	q= y*y
	r=math.sqrt(p+q)
	return r

print "arg strings are:", sys.argv[0],sys.argv[1],sys.argv[2]
x = func(int(sys.argv[1]),int(sys.argv[2]))
#x = func(sys.argv[1],sys.argv[2]) #this does not work as args are strings
print x
