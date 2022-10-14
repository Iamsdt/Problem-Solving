from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0 or len(arr) == 1:
            return [-1]

        m = max(arr[1:])

        for i in range(len(arr)):
            if arr[i] == m:
                m= max(arr[i+1:]) if len(arr[i+1:]) else -1
            
            arr[i] = m

        return arr


if __name__ == "__main__":
    print(Solution().replaceElements([400]))