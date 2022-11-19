from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,val1,val2):
        self.graph[val1].append(val2)
        self.graph[val2].append(val1)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def dfs(self, v):
        visited = set()
        self.DFSUtil(v, visited)

#driverccode
# Driver code
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(0)