from typing import List


class Solution:
    def findAnagrams(self, s:str, p:str)->List[int]:
        if len(p) > len(s): return []

        pCount, sCount = {}, {}

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        # check first one is anagram or not
        # res = [0] if sCount == pCount else []
        res = []
        if sCount == pCount:
            res = [0]

        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            # if the value is zero then remove that
            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            # update pointer
            l += 1

            if pCount == sCount:
                res.append(l)

        return res