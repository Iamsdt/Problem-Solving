"""
# handy if there are so many similar elements

Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing).
Then do some arithmetic to calculate the position of each object in the output sequence.

Ways (simplified):
•    create an count array with size max element and save count based on index
•    on count array do prefix sum (n+(n-1)
•    iterate from end and get the index from count array, subtract with -1,
•    save in the new array, and dont forget to reduce count from count array

Complexity: (Time Space trade off)
- Time: O(n+k)
- Space: O(n) or o(k) -> k means largest element in the array
"""

import random


def count_sort(arr):
    m = max(arr)
    count = [0] * (m + 1)

    for i in arr:
        count[i] += 1

    for i in range(1, m + 1):
        count[i] = count[i - 1] + count[i]

    sort = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        sort[count[arr[i]] - 1] = arr[i]
        count[arr[i]] = count[arr[i]] - 1

    return sort


if __name__ == "__main__":
    inp = [random.randint(0, 5) for _ in range(20)]
    print(inp)
    res = count_sort(inp)
    print(res)
