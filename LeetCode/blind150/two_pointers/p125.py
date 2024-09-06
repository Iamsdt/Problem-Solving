class Solution:
    def isPalindrome(self, s: str) -> bool:
        p, q = 0, len(s)-1

        while p < q:
            if not s[p].isalpha():
                p += 1
                continue

            if not s[q].isalpha():
                q -= 1
                continue

            if s[p].lower() != s[q].lower():
                return False

            # update
            p += 1
            q -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("race a car"))
