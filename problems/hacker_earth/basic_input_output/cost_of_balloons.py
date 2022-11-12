n = int(input())

for i in range(n):
    price = input().split()
    # first case
    # first problem rewards green ballon
    if i %2 == 0:
        # lets get the price
        green = int(price[0])
        purple = int(price[1])
    # second case problem rewards purple ballon
    else:
        green = int(price[1])
        purple = int(price[0])

    # number of pertinent
    num = int(input())
    cost = 0
    for i in range(num):
        res = input().split()
        cost += int(res[0]) * green
        cost += int(res[1]) * purple

    print(cost)

