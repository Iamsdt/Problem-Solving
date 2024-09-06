from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p, q = 0, len(numbers) - 1

        while p < q:
            if numbers[p] + numbers[q] == target:
                return [p+1, q+1]

            if numbers[p] + numbers[q] < target:
                p += 1
            else:
                q -= 1

        return None


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 3, 4, 15], 6))
