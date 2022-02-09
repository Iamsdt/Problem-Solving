from collections import defaultdict
d = defaultdict(list)

n, m = map(int,input().split())
# take a
[d[input()].append(i+1) for i in range(n)]
# take b and also check at the same time
for i in range(m):
    print(*d[input()] or [-1])
