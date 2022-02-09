code = input() #"12X345-67"
# take first two
first = int(code[0]) + int(code[1]) % 2
# now check later
vowels = ["A","E","I","O","U","Y"]

# now check
second = int(code[3]) + int(code[4]) % 2
third = int(code[4]) + int(code[5]) % 2
fourth = int(code[7]) + int(code[8]) % 2
if first+second+ third+ fourth == 0 and  code[2] in vowels:
    print("valid")
else:
    print("invalid")