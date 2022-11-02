
# Hacking solution: But does't work in real world
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)

        return -1

# first approach
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack)+ 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i

        return -1    

    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack)+ 1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1 


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.strStr(haystack="aaa",needle="bb"))