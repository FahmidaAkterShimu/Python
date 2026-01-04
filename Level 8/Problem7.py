# Write a python function to remove a given word from a list ad strip it at the same time. 

def rmv(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))    # It will work only for removing first or last part of any word
    return n

l = ["Shimu", "Shova", "Emu", "mu"]
print(rmv(l, "mu"))

# To Remove any part from any position

def rmv(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.replace(word,""))
    return n
l = ["Shimu", "Shova", "Emu", "mu"]
print(rmv(l, "ho"))
