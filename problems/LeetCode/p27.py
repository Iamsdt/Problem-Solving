class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p, q = 0, len(nums)-1
        count = 0
        while p < len(nums) and q < len(nums):
            if nums[p] == val:
                count += 1
                nums[p], nums[q] = nums[q], '_'
                q -= 1
            else:
                p += 1

        return len(nums) - count

    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
                nums[k] = nums[i]

        return k

if __name__ == '__main__':
    print(Solution().removeElement([1, 2, 3, 4, 3, 3], 3))
    print(Solution().removeElement([3,2,2,3], 3))
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
    