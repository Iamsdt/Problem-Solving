class Solution:
    def numDecodings2(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s)-1, -1, -1):
            print(i)
            if s[i] == '0':
                dp[i] =0
            else:
                dp[i] = dp[i+1]

            if i+1 < len(s) and (s[i] == "1" or s[i]=="2" and int(s[i+1]) <= 6):
                dp[i] += dp[i+2]

            print(dp)

            
        return dp[0]


    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or  s[i] == "2" and int(s[i+1]) <= 6)):
                res += dfs(i+2)
            dp[i] = res
            return res

        return dfs(0)


# what about return all words
class Solution2:
    def numDecodings(self, s: str) -> int:
        di = {}
        for i in range(65, 91):
            di[str(i-64)] = chr(i)

        visited = {}
        def dfs(value):
            if value in visited:
                return visited[value]

            if len(value) == 0 or value[0] == '0':
                return ""
            if len(value) > 1 and value[0] == '2' and int(value[1]) >6:
                return ""
            res = ""
            if value in di:
                res += di[value]
                visited[value] = di[value]
            elif value[0] in di:
                res += di[value[0]]
                visited[value[0]] = di[value[0]]
            
            return res + dfs(value[:1]) + dfs(value[1:])

        return dfs(s)

if __name__ == "__main__":
    print(Solution().numDecodings("226"))
    print(Solution2().numDecodings("226"))