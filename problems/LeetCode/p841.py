import collections


class Solution(object):
    def canVisitAllRooms(self, rooms):
        graph= collections.defaultdict(set)
        for i in range(len(rooms)):
            l=rooms[i]
            for nei in l:
                graph[i].add(nei)
        
        visited=[False for _ in range(len(rooms))]
        visited[0]=True

        def dfs(node):
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        
        dfs(0,graph,visited)
        
        for i in range(len(rooms)):
            if visited[i]==False:
                return False
        return True