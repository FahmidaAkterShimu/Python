s1 = {1, 45, 50, 7}
s2 = {3, 5, 45, 7}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))

print({1,3}.issubset(s1))