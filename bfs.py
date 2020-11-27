from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def BFS(self, vertex):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(vertex)
        visited[vertex] = True

        while queue:
            vertex = queue.pop(0)
            print (vertex, "")
            for i in self.graph[vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
