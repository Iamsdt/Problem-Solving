from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)

        def check(i, k, dp):
            if (i, k) in dp:
                return dp[(i, k)]
            if k == d: return max(jobDifficulty[i:])
            res = float('inf')
            cur = 0
            for j in range(i, n - d + k):
                cur = max(cur, jobDifficulty[j])
                res = min(res, cur + check(j + 1, k + 1, dp))

            dp[(i, k)] = res
            return res

        return -1 if n < d else check(0, 1, {})