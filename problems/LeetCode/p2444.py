from typing import List


class Solution2:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = -1
        p, q = -1, -1
        count = 0
        
        for i in range(len(nums)):
            if nums[i] >= minK and nums[i] <= maxK:
                p = i if nums[i] == minK else p
                q = i if nums[i] == maxK else q
                count += max(0, min(p, q) - left)
            else:
                left = i
                p = -1
                q = -1
        
        return count
    

# chatgpt not working
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        start = 0
        count = 0
        for end in range(n):
            if nums[end] >= minK and nums[end] <= maxK:
                count = end - start + 1
                ans += count
            elif nums[end] > maxK:
                start = end + 1
                count = 0
            elif nums[end] >= nums[start] and nums[end] < minK:
                ans += count
            elif nums[end] < nums[start]:
                start = end
                count = 0
        return ans


    
    
if __name__ == '__main__':
    print(Solution().countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
    print(Solution().countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))
    print(Solution().countSubarrays(nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913],
                                    minK = 35054, maxK = 945315))
    
