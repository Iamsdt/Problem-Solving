from typing import List


class Solution2:
    def calculate_cost(self, nums, cost, target):
        total_cost = 0
        for i, v in enumerate(nums):
            ct = cost[i]
            total_cost += abs(v - target) * ct

        return total_cost

    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # calculate cost for the max number
        mc = float("inf")
        for i in nums:
            value = self.calculate_cost(nums, cost, i)
            mc = min(mc, value)

        return mc


# not optimized for memory
class Solution:
    def calculate_cost(self, nums, cost, target):
        total_cost = 0
        for i, v in enumerate(nums):
            total_cost += abs(target - v) * cost[i]

        return total_cost

    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # calculate cost for the max number
        p, q = min(nums), max(nums)+1

        # run binary search between min value and max value
        while p < q:
            mid = (p+q) // 2

            value1 = self.calculate_cost(nums, cost, mid)
            value2 = self.calculate_cost(nums, cost, mid+1)

            if value1 < value2:
                q = mid
            else:
                p = mid+1

        return self.calculate_cost(nums, cost, p)


if __name__ == "__main__":
    print(Solution().minCost(
        cost=[612038, 351545, 413813, 455422, 507754, 391190,
              760845, 523127, 854280, 21802, 801360, 682463, 845779],
        nums=[348417, 981862, 507335, 474537, 26633, 986541,
              859441, 582902, 866561, 887385, 470146, 928812, 3510]
    ))

    print(Solution().minCost(
        nums=[2, 2, 2, 2, 2],
        cost=[4, 2, 8, 1, 3]
    ))
