from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def DFS_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, "")

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.DFS_util(neighbour, visited)


    def DFS(self, vertex):
        visited = set()
        self.DFS_util(vertex, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
