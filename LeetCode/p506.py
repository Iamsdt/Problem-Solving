import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = []
        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))

        rank = [0] * n
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place <= 3:
                if place == 1:
                    rank[original_index] = "Gold Medal"
                elif place == 2:
                    rank[original_index] = "Silver Medal"
                else:
                    rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)

            place += 1

        return rank


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRelativeRanks([5, 4, 3, 2, 1]))
    print(sol.findRelativeRanks([10, 3, 8, 9, 4]))
