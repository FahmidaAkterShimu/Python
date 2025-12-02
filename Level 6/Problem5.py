# Write a program which finds out whether a given name is present in a list or not.
list= ["Shimu", "Fahmida", "Emon", "Ema", "Emrul", "Smita"]

name= input("Enter a name: ")
if(name in list):
    print("The name is Present in the list.")
else:
    print("The name is not Present in the list.")