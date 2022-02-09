from collections import OrderedDict

items = OrderedDict()

n = int(input())
for i in range(n):
    inp = input().split()
    price = int(inp[-1])
    name = " ".join(inp[:-1])

    if name in items:
        items[name] = items[name] + price
    else:
        # this is first time
        items[name] = price

# # now output
for i in items:
    print(i, items[i])