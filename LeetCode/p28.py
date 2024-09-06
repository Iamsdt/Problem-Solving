
# Hacking solution: But does't work in real world
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)

        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        # handle odd case
        if len(needle) >= len(haystack):
            return 0 if needle == haystack else -1
        
        q = 0
        while q < len(haystack):
            v = haystack[q: q + len(needle)]
            if v == needle:
                return q
            q += 1
        
        return -1

# two pointer
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        # handle odd case
        p, q = len(needle), len(haystack)
        if p > q:
            return -1
        
        # i hold haystack index, and np needle index
        i = 0
        while i < q:
            x, np = i, 0
            
            while x < q and np < p and haystack[x] == needle[np]:
                if np == p - 1: return i
                np += 1
                x += 1
            
            i += 1
            
        return -1


# Lets implement KMP (Knuth, morris and pratt)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p, q = len(needle), len(haystack)
        if p > q:
            return -1
        
        np = [0] * p
        j = 0
        for i in range(1, p):
            while j > 0 and needle[j] != needle[i]:
                j = np[j - 1]
            if needle[j] == needle[i]:
                j += 1
            np[i] = j
        print(np)
        j = 0
        for i in range(q):
            while j > 0 and needle[j] != haystack[i]:
                j = np[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == p:
                return i - p + 1
        return -1



if __name__ == '__main__':
    # begin
    print(Solution().strStr(haystack = "hello", needle = "ll"))
    # print(Solution().strStr(haystack = "leetcode", needle = "leeto"))
    # print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
    # print(Solution().strStr(haystack = "aaa", needle = "aaaa"))
    # print(Solution().strStr(haystack = "mississippi", needle = "issip"))
    # print(Solution().strStr(haystack = "mississippi", needle = "issipi"))
    
    
# 6 , 97, 29, 49