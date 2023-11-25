def VisitNeighbours(node, Graph, weights, queue, visited):
    for i in Graph[node].keys():
        cumulatedCost = weights[node] + Graph[node][i]
        weights[i] = min( weights[i], cumulatedCost )
        if not visited[i] and i not in queue:
            queue.append(i)

def Dijkstra(Graph, start):
    size = len(Graph)
    weights = [float("inf")] * size
    weights[start] = 0
    visited = [0] * size

    v = 0 # index for queue
    queue = [start]

    node = start
    while 0 in visited:
        VisitNeighbours(node, Graph, weights, queue, visited)
        visited[node] = 1

        v += 1
        if v == size:
            if 0 in visited:
                print("Graph is not looked through completely!")
            break
        node = queue[v]
    return weights


def Floyd(Graph):
    size = len(Graph)
    dist = [ [float("inf")] * size for s in range(size) ]
    
    for i in range(size):
        for j in range(size):
            if j in Graph[i].keys():
                dist[i][j] = Graph[i][j]
            if j == i:
                dist[i][j] = 0
    
    for k in range(size):
        for i in range(size):
            for j in range(size):
                dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j] )
        for l in range(size):
            if dist[l][l] < 0:
                return -1 # Negative cycle
    return dist


def DFS_iterative(Graph, v, visited, stack):
    visited[v] = 1
    for n in Graph[v]:
        if not visited[n]:
            DFS_iterative(Graph, n, visited, stack)
    stack.insert(0, v)

def Tarjan(Graph):
    size = len(Graph)
    visited = [0] * size
    stack = []
    for v in range(size):
        if not visited[v]:
            DFS_iterative(Graph, v, visited, stack)
    return stack
