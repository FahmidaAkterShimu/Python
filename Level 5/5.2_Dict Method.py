marks = {
    "Shimu": 90,
    "Emu" : 89,
    "Mim" : 87,
    00 : 'Tanha'
}

print(len(marks))
print(marks.items())
print(marks.keys())
print(marks.update({"Mim":85, "Jui":84}))
print(marks)

print(marks.get("Shim"))     # Prints None
print(marks["Shim"])         # Returns an error  