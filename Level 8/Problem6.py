# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    cm = inch * 2.54
    print(f"Centimetre: {cm}cm")

inch = int(input("Enter the measurement in Inches: "))
inch_to_cm(inch)
