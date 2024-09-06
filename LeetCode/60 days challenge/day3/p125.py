import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        # remove space and coma
        r = "".join([i.lower()
                    for i in s if i.lower() in string.ascii_lowercase])

        return r == r[::-1]


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
