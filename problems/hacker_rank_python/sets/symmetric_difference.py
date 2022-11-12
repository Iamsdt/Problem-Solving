# m = input()
ms = set(map(int, "2 4 5 9".split()))

# n = input()
ns = set(map(int, "2 4 11 12".split()))

f = ms.difference(ns)
s =  ns.difference(ms)

out = f.union(s)

for i in sorted(out):
    print(i)