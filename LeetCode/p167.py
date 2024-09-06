from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p, n = 0, len(numbers) -1

        while p < n:
            v = numbers[p]  + numbers[n]
            if v == target:
                return p+1, n+1

            if v < target:
                p += 1
            else:
                n -= 1



if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 13))