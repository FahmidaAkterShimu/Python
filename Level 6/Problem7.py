# Write a program to find out whether a given post is talking about “Shimu” or not.

post = input("Enter the post: ")

if("Shimu".lower() in post.lower()):
    print("This post is talking about Shimu.")
else:
    print("This post is not talking about Shimu.")