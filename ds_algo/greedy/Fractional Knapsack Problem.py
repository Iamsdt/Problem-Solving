"""
Fractional Knapsack Problem
3 types
1. Fractional (Greedy)
2. Bound (0, 1) (DP)
3. UnBound (DP)
"""


def steal(weights, values, wt):
    arr = []
    for i in range(len(weights)):
        arr.append([weights[i], values[i]])

    # using timsort, nlogn
    arr.sort(key=lambda x: x[0], reverse=True)
    res = []
    p = 0
    while p < len(arr) and wt != 0:
        if arr[p][0] > wt:
            p += 1
            continue

        wt -= arr[p][0]
        res.append(arr[p][1])

    return res


if __name__ == "__main__":
    a = [10, 20, 26]
    b = [60, 100, 120]
    print(steal(a, b, 50))
