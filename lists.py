import os

os.system("cls")

# A List is a collection which is ordered and changeable. Allows duplicate members.
names = ["john", "sue", "larry", "mary"]
print(names)

print(names[2])

names[2] = "daddy"
print(names)

names.append("abigail")
print(names)

names.reverse()
print(names)

names.remove("sue")
print(names)

names.pop()
print(names)

names.sort()
print(names)
