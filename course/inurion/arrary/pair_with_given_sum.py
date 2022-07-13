import random


# problem statements
# [1, 2, 3, 5] find which two numbers == target sum

def solution(arr, target):
    """
        Naive approach,
        time complexity n*2
        space complexity 1
        """
    for i in range(len(arr)):
        j = i + 1
        for j in range(i + 1, len(arr)):
            v = arr[i] + arr[j]
            if v == target:
                return i, j
            j += 1

    return -1, -1


# lets improve
def solution2(arr, target):
    """
    Hashmap approach,
    time complexity n
    space complexity n
    if we want to improve time complexity
    """
    di = {}
    for i, v in enumerate(arr):
        left = target - v
        if left in di:
            return di[left], i
        else:
            di[v] = i

    return -1, -1


def solution3(arr, target):
    """
    Sorted array approach,
    time complexity n*logn
    space complexity 1
    if we want to improve both space and time
    """
    arr.sort()  # nlogn
    p, q = 0, len(arr) - 1
    while p < q:
        v = arr[p] + arr[q]
        if v == target:
            return p, q
        if v < target:
            p += 1
        else:
            q -= 1

    return -1, -1


def print_info(arr, v, target):
    res = arr[v[0]] + arr[v[1]]
    print(f"Index: {v[0]}, {v[1]} -> {arr[v[0]]} + {arr[v[1]]} = {res} which is {res == target}")


if __name__ == "__main__":
    arr = [*range(20)]
    random.shuffle(arr)
    target = 35
    print("Naive Approach")
    v = solution(arr, target)
    print_info(arr, v, target)
    print("\nHash Map Approach")
    print("Only improve time complexity, but decrease space complexity")
    v = solution2(arr, target)
    print_info(arr, v, target)
    print("\nTwo pointer with sorted array Approach")
    v = solution3(arr, target)
    print_info(arr, v, target)
