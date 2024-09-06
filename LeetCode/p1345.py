from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        indices = defaultdict(list)
        for i in range(n):
            indices[arr[i]].append(i)

        si = deque()
        visited = [False] * n
        si.append(0)
        visited[0] = True
        steps = 0
        while si:
            size = len(si)
            while size > 0:
                cu = si.popleft()
                size -= 1
                if cu == n - 1:
                    return steps
                
                jumpNextIndices = indices[arr[cu]]
                jumpNextIndices.append(cu - 1)
                jumpNextIndices.append(cu + 1)

                for jumpNextIndex in jumpNextIndices:
                    if 0 <= jumpNextIndex < n and not visited[jumpNextIndex]:
                        si.append(jumpNextIndex)
                        visited[jumpNextIndex] = True

                jumpNextIndices.clear()
            steps += 1
        return -1