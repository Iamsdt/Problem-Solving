from typing import List


class Solution:
    def cal_moves(self, nums, target):
        moves = 0
        for i in nums:
            moves += abs(target - i)

        return moves

    def minMoves2(self, nums: List[int]) -> int:
        p, q = min(nums), max(nums)+1

        while p < q:
            mid = (p+q) // 2
            v1 = self.cal_moves(nums, mid)
            v2 = self.cal_moves(nums, mid+1)
            if v1 < v2:
                q = mid
            else:
                p = mid+1

        return self.cal_moves(nums, p)
