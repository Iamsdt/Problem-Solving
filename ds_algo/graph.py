class GraphTheory(object):
    def __init__(self, edegas):
        self.edegas = edegas
        self.graph_dict = {}
        for start, end in self.edegas:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def check_graph(self):
        print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            # paris
            new_paths = self.get_paths(node, end, path)

            for p in new_paths:
                paths.append(p)

        return paths

    def shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            # paris
            sp = self.shortest_path(node, end, path)
            if sp:
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path


# test
routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

graph = GraphTheory(edegas=routes)
# graph.check_graph()
s = "Mumbai"
e = "New York"
print(f"All possible path between '{s}' and '{e}'", graph.get_paths(s, e))
print("\n\n")
print("Shortest path between '{s}' and '{e}'", graph.shortest_path(s, e))
