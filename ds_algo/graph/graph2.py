def depthFirstSearch(graph, nodes): # time: O(V + E)
    visited = set()
    connectedComponents = 0
    dfsPath = []
    for i in range(1, nodes + 1):
        if i not in visited:
            connectedComponents += 1
            # dfs at i/from i
            visited.add(i)
            dfsPath.append(i)
            stack = [i]
            while stack:
                currentNode = stack[-1]
                stack.pop() # removes the last element
                # explore the neighbouring nodes
                for neighbourNode in graph[currentNode]:
                    if neighbourNode not in visited:
                        visited.add(neighbourNode)
                        stack.append(neighbourNode)
                        dfsPath.append(neighbourNode)
    return dfsPath # return connectedComponents