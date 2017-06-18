from copy import deepcopy
l1 = [1, 2, 3, "hallo", 5, 6]

l2 = deepcopy(l1);
l2[1]=0
print (l1, l2)

