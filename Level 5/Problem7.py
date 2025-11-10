# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
print(s)

# In python this code will not work at all because sets only contain hashable(immutable) objects
s = {8, 7, 12, "Harry", (1,2)}
# We can use a tuple instead of a list, but we can not change the tuple later.
