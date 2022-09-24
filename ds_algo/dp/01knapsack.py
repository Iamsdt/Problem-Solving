def steal(w, v, wt, n):
    if n == 0 or wt == 0:
        return 0
    print("I am running")
    if w[n - 1] <= wt:
        return max(v[n - 1] + steal(w, v, wt - w[n - 1], n - 1), steal(w, v, wt, n - 1))
    else:
        return steal(w, v, wt, n - 1)


if __name__ == "__main__":
    weight = [2, 4, 5, 7]
    value = [4, 8, 10, 12]
    print(steal(weight, value, 9, len(weight)))
