from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = False

        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if count:
                return False

            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            count = True
            
        
        return True


if __name__ == "__main__":
    print(Solution().checkPossibility([3,4,2,3]))