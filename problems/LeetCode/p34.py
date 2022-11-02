from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        def search(leftBias):
            p, q = 0, len(nums)-1
            i = -1
            while p <= q:
                mid = (p+q)//2
                if target > nums[mid]:
                    p = mid +1 
                elif target < nums[mid]:
                    q = mid-1
                else:
                    i = mid
                    if leftBias:
                        q = mid - 1
                    else:
                        p = mid + 1

            return i

        left = search(True)   
        right = search(False)
        return [left, right]



        
if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8))
    # print(Solution().searchRange([5,7,7,8,8,10], 6))
    # print(Solution().searchRange([], 0))
