from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lets use bucket sorts
        # but use index as values
        di = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for key, value in di.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            res += freq[i]
            if len(res) >= k:
                return res

        return res


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
