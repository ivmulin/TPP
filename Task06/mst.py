""" Module contains Prim's and Kruskal algorithms """


class Queue:
    """ Queue """

    def __init__(self, size, s=0):
        """ Set up queue """
        self.queue = list(range(size))
        self.keys = [float("inf")] * size
        self.tracked = []
        self.keys[s] = 0
        self._n: int

    def extract_min(self):
        """ Extracts minimal key """
        m = float("inf")
        i = 0
        for index, elem in enumerate(self.queue):
            #       for v in range(len(self.queue)):
            if self.keys[index] < m and \
                    elem not in self.tracked:
                m = self.keys[index]
                i = index
        q = self.queue[i]
        self.tracked.append(q)
        return q

    def is_empty(self):
        """ Tells if Queue is empty """
        return len(self.tracked) == len(self.queue)

    def __iter__(self):
        """ Queue's iterator """
        self._n = 0
        return self

    def __next__(self):
        """ Queue.__iter__ brother """
        if self._n < len(self.queue):
            self._n += 1
            return self.queue[self._n-1]
        raise StopIteration


def prim(graph, s=0):
    """ Prim's algorithm """
    size = len(graph)
    tails = [None] * size
    tails[s] = s

    queue = Queue(size, s)
    tree = []

    v = queue.extract_min()
    while not queue.is_empty():
        for u in graph[v]:
            if u in queue and queue.keys[u] > graph[v][u]:
                queue.keys[u] = graph[v][u]
                tails[u] = v
        v = queue.extract_min()
        tree.append((tails[v], v))

    return tree


def finnd_shortest_edge(graph, connected):
    """ Finds shortest edge if it's not in connected """
    minpath, edge = float("inf"), []
    for vertex, elem in enumerate(graph):
        for k, v in elem.items():
            pair = sorted([vertex, k])
            if v < minpath and pair not in connected:
                edge, minpath = pair, v
    return edge, minpath


def amount_of_edges(graph):
    """ Counts amount of edges of a graph """
    a = 0
    for i in graph:
        a += len(i)
    return a // 2  # каждое ребро посчитано дважды


def kruskal(graph):
    """ Kruskal's algorithm """
    size = len(graph)
    forest = []
    connected_vertices = set()
    isolated_edges = {}
    edges = amount_of_edges(graph)

    for i in range(edges):
        edge, _ = finnd_shortest_edge(graph, forest)
        if edge[0] in connected_vertices and edge[1] in connected_vertices:
            continue
        if edge[0] not in connected_vertices and edge[1] not in connected_vertices:
            isolated_edges[edge[0]] = isolated_edges[edge[1]] = edge.copy()
        else:
            if not isolated_edges.get(edge[0]):
                isolated_edges[edge[1]].append(edge[0])
                isolated_edges[edge[0]] = isolated_edges[edge[1]]
            else:
                isolated_edges[edge[0]].append(edge[1])
                isolated_edges[edge[1]] = isolated_edges[edge[0]]

        forest.append(edge)
        connected_vertices.add(edge[0])
        connected_vertices.add(edge[1])

    for i in range(size):
        for j in graph[i]:
            if j not in isolated_edges[i]:
                forest.append(sorted([i, j]))
                branch = isolated_edges[i]
                isolated_edges[i] += isolated_edges[j]
                isolated_edges[j] += branch

    return forest
