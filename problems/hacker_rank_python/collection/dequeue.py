from collections import deque

d = deque()

for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*inp[1:])
    
[print(x, end=' ') for x in d]
