from collections import Counter

number = int(input())
shoes = map(int, input().split())
shoes_dict = Counter(shoes)

cn = int(input())

total = 0
for i in range(cn):
    inp = input().split()
    size = int(inp[0])
    price =  int(inp[1])
    # check size available or not
    if size not in shoes_dict.keys():
        continue
    
    # check stock available or not
    av = shoes_dict[size]
    if (av==0):
        continue

    # lets buy this
    shoes_dict[size] = av - 1
    total += price


print(total)