class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join([ch.lower() for ch in s if ch.isalpha() or ch.isdigit()])
        return res == "".join(reversed(res))


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))


