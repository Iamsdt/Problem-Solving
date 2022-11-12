"""
Array should be sorted


Complexity:
Time: log3N
Space: O(1)
"""


def tenary_search(arr, target):
    s, e = 0, len(arr) - 1
    while s < e:
        mid1 = ((2 * s) + e) // 3
        mid2 = ((2 * e) + s) // 3
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2

        # now update pointers
        if arr[mid1] < target:
            s = mid1 + 1
        else:
            e = mid1 - 1
            continue

        if arr[mid2] < target:
            s = mid2 + 1
        else:
            e = mid2 - 1

    return -1


if __name__ == "__main__":
    inp = [*range(1, 50, 2)]
    print(inp)
    out = tenary_search(inp, 35)
    print(out)
