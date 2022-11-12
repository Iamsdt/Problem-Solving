from collections import defaultdict

edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, ind):
        # TIME AND SPACE COMPLEXITY
        # (V, E)
        # O(v) space complexity
        # Time Complexity
        # O(V+E)
        visited = [False] * (max(self.graph) + 1)
        queue = [ind]
        visited[ind] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, ind):
        visited = [False] * (max(self.graph) + 1)
        queue = [ind]
        visited[ind] = True
        while queue:
            s = queue.pop()
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs_helper(self, s, visited):
        stack = []
        stack.append(s)
        while stack:
            s = stack.pop(-1)
            if not visited[s]:
                print(s, end=" ")
                visited[s] = True
            for i in self.graph[s]:
                if not visited[i]:
                    stack.append(i)

    def disconnected(self):
        visited = [False] * (max(self.graph) + 1)
        for i in self.graph.keys():
            if not visited[i]:
                self.dfs_helper(i, visited)


if __name__ == "__main__":
    g = Graph()
    for i, j in edges:
        g.add_edge(i, j)

    print(g.bfs(0))
    print(g.dfs(0))
