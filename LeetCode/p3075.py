from typing import List


class Solution:
    def maximumHappinessSum2(self, happiness: List[int], k: int) -> int:
        steps = -1
        visited = set()
        result = 0
        for i in range(k):
            steps += 1
            value = -1
            index = -1
            for jj, vv in enumerate(happiness):
                if jj in visited:
                    continue

                # check max
                if value <= vv:
                    value = max(value, vv)
                    index = jj

            visited.add(index)
            im = value - steps
            result += im if im > 0 else 0

        return result

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for turn, score in enumerate(happiness):
            if k == turn:
                return res
            res += max(0, score - turn)

        return res


if __name__ == '__main__':
    sol = Solution()
    happiness = [2, 83, 62]
    k = 3
    print(sol.maximumHappinessSum(happiness, k))
