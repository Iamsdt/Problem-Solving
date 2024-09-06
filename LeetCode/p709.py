class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for i in s:
            if 65 <= ord(i) <= 90:
                v = 97 + (ord(i)-65)
                ans += chr(v)
            else:
                ans += i

        
        return ans


print(Solution().toLowerCase("AZ&phaBET"))