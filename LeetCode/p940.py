from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        for col in range(len(strs[0])):
            # print(strs[col])
            for row in range(1,len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    res += 1
                    break
        return res



if __name__ == '__main__':
    print(Solution().minDeletionSize(["cba","daf","ghi"]))