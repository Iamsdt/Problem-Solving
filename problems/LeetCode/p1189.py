from collections import Counter


class Solution:
    def maxNumberOfBalloons2(self, text: str) -> int:
        di = {}
        for i in text:
            di[i] = di[i]+1 if i in di else 1

        if 'b' not in di:
            return 0
        
        times = di['b']
        s = "balloon"
        res = 0
        for i in range(times):
            is_found = True
            for j in s:
                if j in di and di[j] > 0:
                    di[j] = di[j] -1
                else:
                    is_found = False
                    break

            if is_found:
                res += 1

        return res

    def maxNumberOfBalloons(self, text: str) -> int:
        count_text  = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        for c in balloon:
            res = min(res, count_text[c] // balloon[c])

        return res


if __name__ == '__main__':
    print(Solution().maxNumberOfBalloons("nlaebolko"))
    print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
    print(Solution().maxNumberOfBalloons("leetcode"))
    