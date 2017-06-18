s = set (['a','b','c','d'])
u = set (['b','c','d','e'])

print "s", s
print "u", u

intersectionset =s&u

print "intersection", intersectionset

unionset =s|u

print "union", unionset

differenceset1 =s-u

print "s-u", differenceset1

differenceset2 =u-s

print "u-s", differenceset2


uniqueelements = u^s

print "unique", uniqueelements

print "is s subset of u", s<=u
print "is s superset of u", s>=u


x = [1,2,3]
y = [1,2]

print
print

print "x",x
print "y",y


print "is x subset of y", x<=y
print "is x superset of y", x>=y
print "is y superset of x", y>=x
