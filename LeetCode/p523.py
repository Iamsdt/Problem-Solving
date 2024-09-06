from typing import List


class Solution:
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        def check(n):
            p = 0
            q = n
            while q <= len(nums):
                v = sum(nums[p:q])
                if v % k == 0 or v == 0: return True
                p += 1
                q += 1

            return False

        
        for i in range(2, len(nums)+1):
            ans = check(i)
            if ans:
                return True

        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        total = 0

        for i , n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return  False



if __name__ == '__main__':
    print(Solution().checkSubarraySum([0, 0], 1))