def reverse(arr):
    res = []
    if len(arr) == 1:
        res.append(arr[0])
        return res

    v = arr.pop(-1)
    res.append(v)

    res += reverse(arr)

    return res


if __name__ == "__main__":
    out = reverse([1, 2, 3, 4])
    print(out)
