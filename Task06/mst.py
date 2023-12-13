class Queue:
    def __init__(self, size, s=0):
        self.queue = list(range(size))
        self.keys = [float("inf")] * size
        self.tracked = []
        self.keys[s] = 0

    def ExtractMin(self):
        global iteration
        m = float("inf")
        i = 0
        for v in range(len(self.queue)):
            if self.keys[v] < m and \
                    self.queue[v] not in self.tracked:
                m = self.keys[v]
                i = v
        q = self.queue[i]
        self.tracked.append(q)
        return q

    def isEmpty(self):
        return len(self.tracked) == len(self.queue)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self.queue):
            self._n += 1
            return self.queue[self._n-1]
        raise StopIteration


def Prim(G, s=0):
    size = len(G)
    tails = [None] * size
    tails[s] = s

    queue = Queue(size, s)
    tree = []

    v = queue.ExtractMin()
    while not queue.isEmpty():
        for u in G[v]:
            if u in queue and queue.keys[u] > G[v][u]:
                queue.keys[u] = G[v][u]
                tails[u] = v
        v = queue.ExtractMin()
        tree.append((tails[v], v))

    return tree


def FindShortestEdge(G, connected):
    minpath, edge = float("inf"), list()
    for e in range(len(G)):
        for k, v in G[e].items():
            pair = sorted([e, k])
            if v < minpath and pair not in connected:
                edge, minpath = pair, v
    return edge, minpath


def AmountOfEdges(G):
    a = 0
    for i in G:
        a += len(i)
    return a // 2  # каждое ребро посчитано дважды


def Kruskal(G):
    size = len(G)
    forest = []
    connectedVertices = set()
    connectedEdges = []
    isolatedEdges = {}
    edges = AmountOfEdges(G)

    for i in range(edges):
        edge, _ = FindShortestEdge(G, forest)
        if edge[0] in connectedVertices and edge[1] in connectedVertices:
            continue
        if edge[0] not in connectedVertices and edge[1] not in connectedVertices:
            isolatedEdges[edge[0]] = isolatedEdges[edge[1]] = edge.copy()
        else:
            if not isolatedEdges.get(edge[0]):
                isolatedEdges[edge[1]].append(edge[0])
                isolatedEdges[edge[0]] = isolatedEdges[edge[1]]
            else:
                isolatedEdges[edge[0]].append(edge[1])
                isolatedEdges[edge[1]] = isolatedEdges[edge[0]]

        forest.append(edge)
        connectedVertices.add(edge[0])
        connectedVertices.add(edge[1])

    for i in range(size):
        for j in G[i]:
            if j not in isolatedEdges[i]:
                forest.append(sorted([i, j]))
                branch = isolatedEdges[i]
                isolatedEdges[i] += isolatedEdges[j]
                isolatedEdges[j] += branch

    return forest
