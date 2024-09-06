from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = Counter(nums)

        item = 0
        value = 0

        for i in di.keys():
            m = max(item, di[i])
            if item <= m:
                value = i

        return value

    # Boyer–Moore Majority vote algorithm
    def maxElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

            if count == 0:
                candidate = nums[i]
                count = 1
        
        return candidate


if __name__ == '__main__':
    print(Solution().maxElement([4,1,2,1,2, 2]))