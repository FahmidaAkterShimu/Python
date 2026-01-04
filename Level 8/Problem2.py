# Write a python program using function to convert Celsius to Fahrenheit.
# c/5 = (f-32)/9

def c_to_f(c):
    f = ((c*9)/5) + 32
    print(f"In Fahrenheit Scale: {round(f,2)}F")

c = int(input("Enter the Temperature in Celsius: "))
c_to_f(c)
