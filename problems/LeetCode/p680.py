# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class Solution:
    def validPalindrome(self, s: str) -> bool:
        p, q = 0, len(s)-1
        while p < q:
            if s[p] != s[q]:
                sl, sr = s[p+1:q+1], s[p:q]
                return (sl == sl[::-1] or sr == sr[::-1])

            p, q = p+1, q-1

        return True

            


if __name__ == '__main__':
    print(Solution().validPalindrome('aydmda'))