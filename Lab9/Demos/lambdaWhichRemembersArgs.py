def embed (x,y):
   return ( lambda f:
		f (x,y) )

def first (a,b):
	return a

def second (a,b):
	return b

obj = embed (10,20)

val1 = obj (first)

val2 = obj (second)

print   val1
print	val2
