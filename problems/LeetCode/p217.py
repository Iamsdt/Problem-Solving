from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = {}
        for i in nums:
            if i in di:
                di[i] = di[i] + 1
            else:
                di[i] = 1

        status = False
        for i in di.keys():
            if di[i] > 1:
                status = True
                break

        return status

    def containsDuplicate2(self, nums: List[int]) -> bool:
        di = {}
        for i in nums:
            if i in di:
                return True
            else:
                di[i] = 1

        return False




if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4]))