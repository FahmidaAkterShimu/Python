# Check that a tuple type cannot be changed in python.

a = (34, 334, "Shimu")

a[2] = "Shova"      # Will give an error for this line as tuple cannot be changed
print(a)