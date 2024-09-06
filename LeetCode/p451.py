from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        items = list(ctr.items())
        items.sort(key = lambda x: (-x[1], x[0]))
        words = [ch*n for ch, n in items]
        return ''.join(words)




if __name__ ==  '__main__':
    print(Solution().frequencySort("Aabb"))