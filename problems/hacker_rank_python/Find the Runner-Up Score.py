if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    li = list(arr)
    m = max(li)
    while m in li:
        li.remove(m)

    print(max(li))
