from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        print(Counter(c1.values()))
        print(set(c1.keys()))
        return Counter(c1.values())==Counter(c2.values()) and set(c1.keys())==set(c2.keys())




if __name__ ==  '__main__':
    print(Solution().closeStrings("abc", 'bca'))