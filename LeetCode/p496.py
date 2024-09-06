from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        ind = {n:i for i, n in enumerate(nums1)}

        for i in range(len(nums2)):
            if nums2[i] not in ind:
                continue

            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = ind[nums2[i]]
                    res[idx] = nums2[j]
                    break

        return res


if __name__ == '__main__':
    print(Solution().nextGreaterElement([4,1,2],[1,3,4,2] ))