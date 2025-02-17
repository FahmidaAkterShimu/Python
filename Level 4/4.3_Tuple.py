a = (1,2,3,4,3)     # Tuple is immutable
print(a)
print(type(a))

b =()           # Empty tuple
print(b)
print(type(b))

c = (1)         # This is not a tuple of one element
print(c)
print(type(c))

d = (1,)        # One element tuple have to be written using comma 
print(d)
print(type(d))

no = a.count(3)
print("Count of number 3 are: ", no)

i = a.index(3)
print(i) 

print(5 in a)