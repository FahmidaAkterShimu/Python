# Write a recursive function to calculate the sum of first n natural numbers. 

n = int(input("Enter the number: "))

def sum(n):
    if (n==1):
        return 1
    return n + sum(n-1)

print(f"The Sum of first n natural numbers: {sum(n)}")
