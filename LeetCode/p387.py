
class Solution(object):
    def firstUniqChar(self, s):
        for i in range(len(s)):
            print(s[i], s[:i]+s[i+1:])
            if s[i] not in s[:i]+s[i+1:]:
                return i
        return -1


print(Solution().firstUniqChar("loveleetcode"))
