# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if (a>b and a>c):
        print("a is the greatest number")
    elif(b>a and b>c):
        print("b is the greatest number")
    else:
        print("c is the greatest number")

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

greatest(a, b, c)
