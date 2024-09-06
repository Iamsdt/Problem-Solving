from functools import cache
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        @cache
        def dfs(i, dist):
            if i == len(cookies):
                return max(dist)

            nd = list(dist)
            ans = float('inf')
            for j in range(k):
                nd[j] += cookies[i]
                sub = dfs(i+1, tuple(sorted(nd)))
                ans = min(ans, sub)
                nd[j] -= cookies[i]

            return ans

        return dfs(0, (0,)*k)


if __name__ == "__main__":
    print(Solution().distributeCookies([8, 15, 10, 20, 8], k=2))
