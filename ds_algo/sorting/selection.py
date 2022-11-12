import random

"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element
(considering ascending order) from unsorted part and putting it at the beginning.

Ways (simplified):
# keep two part sorted and unsorted
# in every iteration take a fixed position and swap with rest of the values values
# when one iteration done, move that fixed position in sorted array 
(basically increase fixed position)  

1. iterate -> same as array length
2. now in every iteration
take a fixed position and swap the value with the pointer position, if required

Complexity:
- Time: O(n2)
- Space: O(1)
"""


def selection(arr):
    fixed, p = 0, 1
    while fixed < len(arr):
        while p < len(arr):
            if arr[p] < arr[fixed]:
                arr[fixed], arr[p] = arr[p], arr[fixed]

            p += 1
        # when loop done
        fixed += 1


def selection2(arr):
    for i in range(len(arr)):
        fixed = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[fixed]:
                arr[fixed], arr[j] = arr[j], arr[fixed]


if __name__ == "__main__":
    inp = [*range(20)]
    random.shuffle(inp)
    print(inp)
    selection(inp)
    print(inp)
