from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rs = Counter(ransomNote)
        mg = Counter(magazine)

        for i in rs.keys():
            a = rs[i]
            b = mg.get(i, 0)
            print(a, b)
            if a > b:
                return False

        return True


if __name__ == "__main__":
    print(Solution().canConstruct("a", "b"))
    print(Solution().canConstruct("aa", "ab"))
    print(Solution().canConstruct("aa", "aab"))
