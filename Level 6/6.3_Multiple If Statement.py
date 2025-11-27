a = int(input("Enter your age: "))

# If statement No.1
if(a<=0):
    print("Your age is Invalid.")
elif(a%2==0):
    print("Your age is Even.")    
else:
    print("Your age is Odd.")

# If statement No.2
if(a>=18):
    print("You are above the age of consent.")
    print("Good for you.")

elif(a<=0):
    print("You are entering an invalid age.")

else:
    print("You are below the age of consent.")

print("End of program.")