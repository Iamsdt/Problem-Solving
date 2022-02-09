# Time Limit Exceeded

# N = int(input())
# data = [int(x) for x in input().split()]

# number = 0

# for i in range(len(data)):
#     a = data[i]
#     v = a - (a//10) * 10
#     number += v * (10 ** (N-(i+1)))


# print("Yes" if number % 10 == 0 else "No")


# hacking solution
N = int(input())
data = "".join([x[-1] for x in input().split()])
print("Yes" if int(data) % 10 == 0 else "No")


