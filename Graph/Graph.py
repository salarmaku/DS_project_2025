class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

    def AddVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
            self.vertex_count += 1

    def AddEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            exists = False
            for i in range(len(self.vertices[v1])):
                if self.vertices[v1][i] == v2:
                    exists = True
            if not exists:
                self.vertices[v1] = self.vertices[v1] + [v2]

            exists = False
            for i in range(len(self.vertices[v2])):
                if self.vertices[v2][i] == v1:
                    exists = True
            if not exists:
                self.vertices[v2] = self.vertices[v2] + [v1]

    def RemoveEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1] = self._remove_from_list(self.vertices[v1], v2)
            self.vertices[v2] = self._remove_from_list(self.vertices[v2], v1)

    def RemoveVertex(self, vertex):
        if vertex in self.vertices:
            neighbors = self.vertices[vertex]
            for i in range(len(neighbors)):
                self.vertices[neighbors[i]] = self._remove_from_list(
                    self.vertices[neighbors[i]], vertex
                )
            del self.vertices[vertex]
            self.vertex_count -= 1

    def BFS(self, start):
        visited = []
        queue = []
        result = ""

        queue = queue + [start]
        visited = visited + [start]

        while len(queue) != 0:
            current = queue[0]
            queue = queue[1:]
            result += str(current) + " "

            neighbors = self.vertices[current]
            for i in range(len(neighbors)):
                if not self._exists(visited, neighbors[i]):
                    visited = visited + [neighbors[i]]
                    queue = queue + [neighbors[i]]

        return result.strip()

    def DFS(self, start):
        visited = []
        result = ""
        result = self._dfs_helper(start, visited, result)
        return result.strip()

    def _dfs_helper(self, vertex, visited, result):
        visited = visited + [vertex]
        result += str(vertex) + " "

        neighbors = self.vertices[vertex]
        for i in range(len(neighbors)):
            if not self._exists(visited, neighbors[i]):
                result = self._dfs_helper(neighbors[i], visited, result)

        return result

    def _exists(self, arr, value):
        for i in range(len(arr)):
            if arr[i] == value:
                return True
        return False

    def _remove_from_list(self, arr, value):
        new_list = []
        for i in range(len(arr)):
            if arr[i] != value:
                new_list = new_list + [arr[i]]
        return new_list

# Test
g = Graph()

g.AddVertex("A")
g.AddVertex("B")
g.AddVertex("C")
g.AddVertex("D")

g.AddEdge("A", "B")
g.AddEdge("A", "C")
g.AddEdge("B", "D")

print("BFS:", g.BFS("A"))
print("DFS:", g.DFS("A"))
