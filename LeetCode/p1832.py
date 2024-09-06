from collections import Counter

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        di = Counter(sentence)
        print(di)
        for i in range(97, 122):
            if chr(i) not in di:
                return False

        return True


if __name__ == '__main__':
    print(Solution().checkIfPangram("onrcsnlxckptsxffbyswujpamfltvmdoxovggepknmtacrjkkorjgvgtgaiaudspnpxkwikevmjeephhiyvnoymjwjfopovscbefecnoytjxfwasabwohqujwowmakpyuuqvgfab"))