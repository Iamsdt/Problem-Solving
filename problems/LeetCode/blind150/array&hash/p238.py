from typing import List


class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            pre *= nums[i]
            prefix[i] = pre

        post = 1
        for i in range(len(nums)-1, -1, -1):
            post *= nums[i]
            postfix[i] = post

        print(nums)
        print(prefix)
        print(postfix)

        # now result
        for i in range(len(nums)):
            pre = prefix[i - 1] if i > 0 else 1
            post = postfix[i+1] if i < len(nums) - 1 else 1
            nums[i] = pre * post

        return nums

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        print(res)

        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
