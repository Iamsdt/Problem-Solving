from heapq import heappush, heappop
from typing import List


class Solution:
    def mincostToHireWorkers(
            self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)
        result = float("inf")
        p = 0
        wage_ratio = []

        for i in range(n):
            heappush(wage_ratio, (wage[i] / quality[i], quality[i]))

        print(wage_ratio)

        quality_worker = []

        for i in range(n):
            ratio, qua = heappop(wage_ratio)
            print(ratio, qua)
            p += qua
            heappush(quality_worker, -qua)
            print(quality_worker)

            if len(quality_worker) > k:
                p += heappop(quality_worker)

            if len(quality_worker) == k:
                print(p, ratio)
                result = min(result, p * ratio)

        return result


if __name__ == "__main__":
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    k = 2
    print(Solution().mincostToHireWorkers(quality, wage, k))