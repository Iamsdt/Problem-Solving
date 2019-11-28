inp = int(input())
list = []
for i in range(inp):
    li = input().split(" ")
    cmd = li[0]
    if cmd == "insert":
        # insert 0 6
        list.insert(int(li[1]), int(li[2]))
    elif cmd == "print":
        print(list)
    elif cmd == "remove":
        # remove 6
        list.remove(int(li[1]))
    elif cmd == "append":
        # append 6
        list.append(int(li[1]))
    elif cmd == "sort":
        list.sort()
    elif cmd == "pop":
        list.pop()
    elif cmd == "reverse":
        list = list[::-1]
