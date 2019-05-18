class Graph:

    def __init__(self, verticesNumber):  # Graph is initialized according to number of vertices
        self.verticesNumber = verticesNumber
        self.graph = [[0 for column in range(verticesNumber)] for row in range(verticesNumber)]
        # creates 2D adjacency matrix initialized to zero

    def MST(self, root):

        infinity = float("inf")  # float value of infinity is stored in variable
        keys = [infinity] * self.verticesNumber  # 1D vector assigns infinite keys to all vertices
        minimumSpanTree = [None] * self.verticesNumber  # initialize minimum spanning tree
        keys[root] = 0  # initialize first vertex key to 0
        minimumSet = [False] * self.verticesNumber  # stores visited vertices
        minimumSpanTree[root] = "habal"  # The root of the tree is initialized
        for vertex in range(self.verticesNumber):

            v = self.minimumIndex(keys, minimumSet)  # pick the unvisited vertex with least weighted distance
            if v == -1:
                print("Graph is disconnected")
                return
            minimumSet[v] = True

            for u in range(self.verticesNumber):
                if self.graph[v][u] > 0 and minimumSet[u] is False and keys[u] > self.graph[v][u]:
                    keys[u] = self.graph[v][u]
                    minimumSpanTree[u] = v

        self.printMST(minimumSpanTree, root)

    def dijkstra(self, vertex):
        infinity = float("inf")
        distances = [infinity] * self.verticesNumber
        distances[vertex] = 0
        shortestPaths = [-1] * self.verticesNumber
        queue = []
        for i in range(self.verticesNumber):
            queue.append(i)
        while queue:
            v = self.minimumDistance(distances, queue)
            if v == -1:
                print("Graph is disconnected")
                return
            queue.remove(v)
            for i in range(self.verticesNumber):
                if self.graph[v][i] > 0 and i in queue:
                    if distances[v] + self.graph[v][i] < distances[i]:
                        distances[i] = distances[v] + self.graph[v][i]
                        shortestPaths[i] = v
        self.printDistances(distances, shortestPaths, vertex)


    def printDistances(self, distances, paths, vertex):
        print("Vertex \t\tDistance\tPath")
        for i in range(len(distances)):
            if i == vertex: continue
            # print("\n%d --> %d \t\t%d \t\t\t\t\t" % (vertex, i, distances[i])),self.printPaths(paths, i)
            print("\n" + str(vertex) + "-->" + str(i) + "\t\t" + str(distances[i]) + "\t\t\t" + str(self.printPaths(paths,i)))

    def printPaths(self, paths, index):
        if paths[index] == -1:
            return str(index)
        return self.printPaths(paths, paths[index]) + "->" + str(index)



    def printMST(self, minimumSpanTree, root):
        totalWeight = 0
        for i in range(self.verticesNumber):
            if i == root:
                continue
            if self.graph[i][minimumSpanTree[i]] == 0:
                print("Graph is disconnected")
                continue
            print(minimumSpanTree[i], "-", i, "\t", self.graph[i][minimumSpanTree[i]])
            totalWeight += self.graph[i][minimumSpanTree[i]]
        print("Total Weight is " + str(totalWeight))

    def minimumIndex(self, values, Set):
        minimum = float("inf")
        minIndex = -1
        for i in range(self.verticesNumber):
            if values[i] < minimum and Set[i] is False:
                minimum = values[i]
                minIndex = i
        return minIndex

    def minimumDistance(self, distances, q):
        minimum = float("inf")
        minIndex = -1
        for i in range(self.verticesNumber):
            if distances[i] < minimum and i in q:
                minimum = distances[i]
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
