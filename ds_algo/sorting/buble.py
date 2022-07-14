import random

"""
Bubble sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly 
swapping the adjacent elements if they are in wrong order.

Ways (simplified):
1. iterate -> same as array length
2. now in every iteration
compare nth number with n+1 th number and swap

Complexity:
- Time: O(n2)
- Space: O(1)
"""


# using while loop
def bubble(arr):
    p, q = 0, len(arr) - 1
    while q != 0:
        p = 0
        while p + 1 < len(arr):
            if arr[p] > arr[p + 1]:
                arr[p], arr[p + 1] = arr[p + 1], arr[p]
            p += 1
        q -= 1


# using for loop
def bubble2(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# using recursion
def bubble3(arr, q=None):
    if not q:
        q = len(arr) - 1

    if q == 1:
        return

    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    bubble3(arr, q - 1)


if __name__ == "__main__":
    inp = [*range(20)]
    random.shuffle(inp)
    print(inp)
    bubble3(inp)
    print(inp)
