class Solution:
    def longestCommonSubsequence(self, text1, text2):
        c = []
        for i in range(len(text1) + 1):
            c.append([0])
            for j in range(len(text2)):
                c[i].append(0)
        for i, t1 in enumerate(text1):
            for j, t2 in enumerate(text2):
                if t1 == t2:
                    c[i + 1][j + 1] = c[i][j] + 1
                else:
                    c[i + 1][j + 1] = max(c[i][j + 1], c[i + 1][j])
        return c[-1][-1]