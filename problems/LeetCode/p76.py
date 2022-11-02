from collections import Counter

# need to understand with window sliding

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        count, window = Counter(t), {}

        have, need = 0, len(count)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count and window[c] == count[c]:
                have += 1

            while have == need:
                if (r-l + 1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)

                # now srink window
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                
                # update pointer
                l += 1

        return s[res[0]: res[1]+1] if resLen !=  float('inf') else ""

