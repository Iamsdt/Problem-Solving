edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
graph = {}

for i, j in edges:
    if i in graph:
        graph[i].append(j)
    else:
        graph[i] = [j]

print(graph)

# 2 WAY
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#
#
# g = Graph()
# for i, j in edges:
#     g.add_edge(i, j)
#
# print(dict(g.graph))

# now with matrix
graph = []
for _ in range(4):
    graph.append([0] * 4)

print(graph)

# now save
for i, j in edges:
    graph[i][j] = 1

print(*graph, sep="\n")
