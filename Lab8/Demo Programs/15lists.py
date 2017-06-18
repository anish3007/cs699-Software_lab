l1 = [1, 2, 3, "hallo", 5, 6]
print (l1)

print ("length of list:", len(l1))

l1 = l1 + l1

print (l1)

s = ""
for item in l1:
	s = s + str(item)

print (s)


l1.append(l1)

last = l1[len(l1)-1]

print (l1)

print (last[0])

