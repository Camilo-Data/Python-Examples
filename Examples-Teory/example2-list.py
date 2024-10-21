a = [1,2,3,4,5,6,7,8,9,0]
b = a 
print(a)
print(b)
del a [0]

print(id(a))
print(id(b))

#slice

c = a[:]

print(id(c))

a.append(11)

print(c)
print(b)