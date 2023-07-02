from functools import cache
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        buildings = [0] * n
        res = [0]

        def check(index, curr):
            if all([j == 0 for j in buildings]):
                res[0] = max(res[0], curr)

            if index == len(requests):
                return

            for i in range(index, len(requests)):
                src, dst = requests[i]
                buildings[src] -= 1
                buildings[dst] += 1

                check(i+1, curr+1)

                buildings[src] += 1
                buildings[dst] -= 1

        check(0, 0)
        return res[0]


if __name__ == "__main__":
    value = [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]
    n = 3
    print(Solution().maximumRequests(n, value))
