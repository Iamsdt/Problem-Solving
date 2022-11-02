# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10,15,20]))