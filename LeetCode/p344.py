from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p,q = 0, len(s)-1
        while p < q:
            s[p], s[q] = s[q], s[p]
            p, q = p + 1, q -1

        return s


if  __name__ == "__main__":
    print(Solution().reverseString(["H","a","n","n","a","h"]))