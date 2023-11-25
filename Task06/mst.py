class Queue:
    def __init__(self, size, s=0):
        self.queue = list( range(size) )
        self.keys = [float("inf")] * size
        self.tracked = []
        self.keys[s] = 0


    def ExtractMin(self):
        global iteration
        m = float("inf")
        i = 0
        for v in range( len(self.queue) ):
            if  self.keys[v] < m and \
                self.queue[v] not in self.tracked:
                m = self.keys[v]
                i = v
        q = self.queue[i]
        self.tracked.append(q)
        return q


    def isEmpty(self):
        return len( self.tracked ) == len( self.queue )


    def __iter__(self):
        self._n = 0
        return self


    def __next__(self):
        if self._n < len( self.queue ):
            self._n += 1
            return self.queue[ self._n-1 ]
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


def AdjacencyList(G):
    size = len(G)
    adjlist = dict()
    for i in range(size):
        for j in G[i].keys():
            a, b = sorted([i, j])
            if (a, b) not in adjlist:
                adjlist[(a, b)] = G[i][j]

    return adjlist

def Raw(structure):
    raw = set()
    for e in structure:
        raw.update( set(e) )
    return raw


def IsAdjacent(forest, tree, x, y):
    if x in Raw(forest[tree]):
        m = x
    else:
        m = y
    for i in range( len(forest) ):
        if i == tree:
            continue
        if  (x in Raw(forest[i]) and m == y) or \
            (y in Raw(forest[i]) and m == x):
            return i
    return None


def Kruskal(G, s=0):
    size = len(G)
    forest = [list()]
    adjmap = AdjacencyList(G)
    adjmap = dict( sorted(adjmap.items(), key=lambda x: x[1]) )
    
    forest[0].append( list(adjmap.keys())[0] )
    for (x, y) in adjmap.keys():
        for t in range( len(forest) ):
            raw = Raw(forest[t])
            if not ( x in raw and y in raw ):

                forest[t].append((x, y))
                adjacent = IsAdjacent(forest, t, x, y)
                if adjacent:
                    forest[t].extend( forest[adjacent] )
                    forest[adjacent].clear()

    return forest
