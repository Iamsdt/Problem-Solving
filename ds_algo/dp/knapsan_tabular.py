def steal(w, v, wt, n, dp):
    if n == 0 or wt == 0:
        return 0
    if dp[n][wt] != -1:
        return dp[n][wt]
    print("I am running")

    if w[n - 1] <= wt:
        dp[n][wt] = max(v[n - 1] + steal(w, v, wt - w[n - 1], n - 1, dp), steal(w, v, wt, n - 1, dp))
        return dp[n][wt]
    else:
        dp[n][wt] = steal(w, v, wt, n - 1, dp)
        return dp[n][wt]


if __name__ == "__main__":
    weight = [2, 4, 5, 7]
    value = [4, 8, 10, 12]
    wt = 9
    # lets create table
    table = []
    for i in range(wt+1):
        res = [-1 for _ in range(len(value)+1)]
        table.append(res)

    print(table)

    dp = []
    for i in range(len(weight) + 1):
        dp.append([-1 for _ in range(wt + 1)])

    print(steal(weight, value, wt, len(weight), dp))
