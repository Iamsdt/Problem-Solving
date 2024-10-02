# Failed IN Leetcode

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                square = s * s
                if target - square < 0:
                    break
                
                dp[target] = min(dp[target], 1 + dp[target-square])
        
        return dp[n]



# Will pass in leetcode
class Solution:
    def numSquares(self, n: int) -> int:
        q=deque()
        visited=set()
        q.append((0,0))
        while q:
            s,count=q.popleft()
            count+=1
            for i in range(1,n+1):
                temp=s+i*i
                if temp>n:
                    break
                if temp==n:
                    return count
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp,count))

      
