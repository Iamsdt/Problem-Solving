import random

"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort 
playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part. 
Values from the unsorted part are picked and placed at the correct position in the sorted part.

Ways (simplified):
keep two parts, sorted array and unsorted array
take any element from unsorted array and find the right position in sorted portion

1. iterate -> same as array length
2. now in every iteration
take an element and iterate until it's find correct position 

Complexity:
- Time: O(n2)
- Space: O(1)
"""


def insertion(arr):
    st, p = 0, 1

    while p < len(arr):
        temp = st
        while temp:
            if arr[p] < arr[temp]:
                arr[temp], arr[p] = arr[p], arr[temp]
                temp -= 1
                continue
            else:
                break
        p += 1


def insertion2(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


if __name__ == "__main__":
    inp = [*range(20)]
    random.shuffle(inp)
    print(inp)
    insertion2(inp)
    print(inp)
