import random


def insert(arr, value):
    if len(arr) == 0 or arr[-1] < value:
        arr.append(value)
        return
    val = arr.pop(-1)
    insert(arr, value)
    arr.append(val)


def sort(arr):
    if len(arr) == 1:
        return
    num = arr.pop(-1)
    sort(arr)
    insert(arr, num)


if __name__ == "__main__":
    inp = [*range(20)]
    random.shuffle(inp)
    print(inp)
    sort(inp)
    print(inp)
