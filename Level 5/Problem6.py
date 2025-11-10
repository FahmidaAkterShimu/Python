# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

print(d)

# If the names of 2 friends are same; what will happen to the program in problem 6?
# It will consider 2 friends as one and update the language from 1st one to 2nd one

# If languages of two friends are same; what will happen to the program in problem 6?
# No trouble will happen. The values can be same.