name = 'Shimu'      # Negative index -5,-4,-3,-2,-1

print(name[-4 : -1])    # Inclue -4,-3,-2 indices and exclude index -1
print(name[1:4])

print(name[:4])     # Same as print(name[0:4]) -->[first ind : 4]
print(name[2:])     # Same as print(name[2:5]) -->[2 : length]

# We can skip any value as a part of our slice like this: 
word = "amazing" 
print(word[1: 6: 2])    # "mzn" 
# print(word[1:6]) --> mazin --> [1:6:2] --> (m)a (z)i (n) 
