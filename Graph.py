class Graph:

    def __init__(self, verticesNumber):  # Graph is initialized according to number of vertices
        self.verticesNumber = verticesNumber
        self.graph = [[0 for column in range(verticesNumber)] for row in range(verticesNumber)]
        # creates 2D adjacency matrix initialized to zero

    def MST(self):

        infinity = float("inf")  # float value of infinity is stored in variable
        keys = [infinity] * self.verticesNumber  # 1D vector assigns infinite keys to all vertices
        minimumSpanTree = [None] * self.verticesNumber  # initialize minimum spanning tree
        keys[0] = 0  # initialize first vertex key to 0
        minimumSet = [False] * self.verticesNumber  # stores visited vertices
        minimumSpanTree[0] = -1  # The root of the tree is initialized
        for vertex in range(self.verticesNumber):

            v = self.minimumIndex(keys, minimumSet) # pick the unvisited vertex with least weighted distance
            minimumSet[v] = True

            for u in range(self.verticesNumber):
                if self.graph[v][u] > 0 and minimumSet[u] is False and keys[u] > self.graph [v][u]:
                    keys[u] = self.graph[v][u]
                    minimumSpanTree[u] = v

        self.printMST(minimumSpanTree)

    def dijkstra(self, vertex):
        infinity = float("inf")
        distances = [infinity] * self.verticesNumber
        distances[vertex] = 0
        shortestPathSet = [False] * self.verticesNumber
        for vertices in range(self.verticesNumber):
            v = self.minimumIndex(distances, shortestPathSet)
            shortestPathSet[v] = True
            for u in range(self.verticesNumber):
                if self.graph[v][u] > 0 and shortestPathSet[u] is False and distances[u] > distances[v] + self.graph[v][u]:
                    distances[u] = distances[v] + self.graph[v][u]
        self.printDistances(distances)

    def printDistances(self, distances):
        for node in range(self.verticesNumber):
            print(str(node) + "\t" + str(distances[node]))


    def printMST(self, minimumSpanTree):
        for i in range(1, self.verticesNumber):
            print(minimumSpanTree[i], "-", i, "\t", self.graph[i][minimumSpanTree[i]])

    def minimumIndex(self, values, Set):
        minimum = float("inf")
        for i in range(self.verticesNumber):
            if values[i] < minimum and Set[i] is False:
                minimum = values[i]
                minIndex = i
        return minIndex


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
