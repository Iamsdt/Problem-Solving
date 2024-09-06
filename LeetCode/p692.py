from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        lst = [(-count, word) for word, count in Counter(words).items()]
        li = heapq.nsmallest(k,lst)
        return [word for _, word in li]


if __name__ == '__main__':
    print(Solution().topKFrequent(["aaa","aa","a"], 1))
    print(Solution().topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 3))
