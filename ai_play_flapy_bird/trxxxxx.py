import copy
a = [1,2,[1,2],3]
b = a
c = a.copy()
d = copy.deepcopy(a)
print(a)
print(b)
print(c)
print(d)
a[0] = 5
print(a)
print(b)
print(c)
print(d)
a[2][0] = 0
print(a)
print(b)
print(c)
print(d)