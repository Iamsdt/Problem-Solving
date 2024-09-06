class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx+1][::-1] + word[idx+1:]


if __name__ == "__main__":
    s = Solution()
    print(s.reversePrefix("abcdef", "d"))
    print(s.reversePrefix("xyxzxe", "z"))
    print(s.reversePrefix("abcd", "z"))
