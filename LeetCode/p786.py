from heapq import heappush, heappop
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        data = []
        n = len(arr)

        # Populate min heap with fractions
        for i in range(n):
            for j in range(i + 1, n):
                fraction = (arr[i] / arr[j], (arr[i], arr[j]))
                heappush(data, fraction)

        # Pop k-1 smallest fractions
        for _ in range(k - 1):
            heappop(data)

        # Return the k-th smallest fraction
        return heappop(data)[1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 3))
