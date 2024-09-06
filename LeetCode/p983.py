from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = float('inf')
            for day, cost in zip([1, 7, 30], costs):
                p = i
                while p < len(days) and days[p] < days[i] + day:
                    p += 1

                cache[i] = min(cache[i], cost + dfs(p))

            return cache[i]

        return dfs(0)


if __name__ == "__main__":
    print(Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
