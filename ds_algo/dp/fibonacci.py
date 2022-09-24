# Recursion vs DP

def rec(n):
    print("Calling with ", n)
    if n == 1:
        return 0
    if n == 2:
        return 1
    return rec(n - 1) + rec(n - 2)


# Memorization approach
# TOP Down
def dp(v, lookup):
    # already calculated
    if lookup[v] != -1:
        return lookup[v]

    print("Calling with ", v)
    if v == 1:
        lookup[v] = 0
        return lookup[v]
    if v == 2:
        lookup[v] = 1
        return lookup[v]

    lookup[v] = dp(v - 1, lookup) + dp(v - 2, lookup)
    return lookup[v]


# Tabulation approach
# Bottom UP
def dp2(v):
    array = [0, 1]
    for i in range(2, v):
        array.append(array[i - 1] + array[i - 2])

    return array[-1]


if __name__ == "__main__":
    n = 6
    print(rec(n))
    print("\n\n Dynamic Programming")
    values = [-1] * (n + 1)
    print(values)
    print(dp(n, values))
    print(values)
    print(dp2(n))
