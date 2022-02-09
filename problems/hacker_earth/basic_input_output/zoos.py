text = input()

# find the index
index = 0
for i in range(len(text)):
    if text[i] == "z":
        index = i

z = text[:index+1]
o = text[index+1:]

if 2 * len(z) == len(o):
    print("Yes")
else:
    print("No")
    