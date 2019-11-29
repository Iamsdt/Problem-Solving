n = int(input())
inp_list = map(n, input().split())
list = [int(x) for x in inp_list]
tup = tuple(list)
print(hash(tup))
