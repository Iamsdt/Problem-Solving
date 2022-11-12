from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = []
        d = {}
        
        for i in range(1, n+1):
            arr.append(i)
            d[i] = []
            
        for i in trust:
            d[i[1]].append(i[0])
            if i[0] in arr:
                arr.remove(i[0])
        
        if len(arr)!=1:
            return -1
        
        for key, value in d.items():
            if key==arr[0] and len(value)==n-1:
                return key
        
        return -1



if __name__ == '__main__':
    # Input: n = 2, trust = [[1,2]]
    # Output: 2
    # Example 2:

    # Input: n = 3, trust = [[1,3],[2,3]]
    # Output: 3
    # Example 3:

    # Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    # Output: -1
    print(Solution().findJudge(2, [[1,2]]))
    print(Solution().findJudge(3, [[1,3],[2,3]]))
    print(Solution().findJudge(3, [[1,3],[2,3],[3,1]]))
    print(Solution().findJudge(3, [[1,2],[2,3]]))
    print(Solution().findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
    