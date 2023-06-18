from queue import Queue
from typing import List

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        visited = [0] * N
        graph = [[] for _ in range(N)]
        for edge in dislikes:
            u = edge[0] - 1
            v = edge[1] - 1
            graph[u].append(v)
            graph[v].append(u)
            
        q = Queue()
        for i in range(0, N):
            if visited[i] != 0:
                continue
            visited[i] = 1
            q.put(i)
            while not q.empty():
                s = q.qsize()
                for j in range(0, s):
                    u = q.get()
                    for k in range(0, len(graph[u])):
                        v = graph[u][k]
                        if visited[v] == 0:
                            visited[v] = 2 if visited[u] == 1 else 1
                            q.put(v)
                        
                        if visited[v] == visited[u]:
                            return False
                    
        return True
            