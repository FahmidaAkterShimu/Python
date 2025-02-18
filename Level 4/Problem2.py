# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

m1 = int(input("Marks of 1st student: "))
marks.append(m1)
m2 = int(input("Marks of 2nd student: "))
marks.append(m2)
m3 = int(input("Marks of 3rd student: "))
marks.append(m3)
m4 = int(input("Marks of 4th student: "))
marks.append(m4)
m5 = int(input("Marks of 5th student: "))
marks.append(m5)
m6 = int(input("Marks of 6th student: "))
marks.append(m6)

print(marks)

marks.sort()
print(marks)

# Marks of 1st student: 45
# Marks of 2nd student: 56
# Marks of 3rd student: 55
# Marks of 4th student: 42
# Marks of 5th student: 67
# Marks of 6th student: 56
# [45, 56, 55, 42, 67, 56]
# [42, 45, 55, 56, 56, 67]