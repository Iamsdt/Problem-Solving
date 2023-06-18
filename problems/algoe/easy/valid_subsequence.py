def isValidSubsequence(array, sequence):
    p = 0
    q = 0

    while p < len(array) and q < len(sequence):
        if array[p] == sequence[q]:
            q += 1

        p += 1

    return q == len(sequence)


if __name__ == "__main__":
    print(isValidSubsequence([5, 4, 3, 2, 22, 1, 56, 78], [3, 2, 1, -1]))
