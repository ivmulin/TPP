def Supersize(G):
    s = 0
    for igor in G:
        s += len(igor)
    return s


def F(G, s=0):
    size = len(G)
    supersize = Supersize(G)
    S = []
    found = 0
    path = []
    tested = 1
    c = 1
    v = s
    while not found:
        for i in G[v]:
            if ( len(G[i]) > 0 and G[i] != {i} ) or tested == supersize:
                path.append(v)
                G[v].remove(i)
                v = i
                tested += 1
                break
        c += 1
        if tested == supersize:
            path.append(v)
            if s in G[v]:
                path.append(s)
                found = 1
    return path


def _W(G, K, s, result):
    for i in G[s]:
        if i in K[s]:
            continue
        K[s].append(i)
        _W(G, K, i, result)
    result.append(s)


def W(G, s=0):
    K = [[None] for i in range(len(G))]
    result = []
    _W(G, K, s, result)
    result = result[::-1]
    return result


def revert(G):
    size = len(G)
    result = [set() for i in range(size)]
    for i in range(size):
        for j in G[i]:
            result[j].add(i)
    return result


def DFSinv(s, visited, G, stack):
    visited[s] = 1
    for i in G[s]:
        if not visited[i]:
            DFSinv(i, visited, G, stack)
    stack.append(s)


def DFS(s, visited, G, result):
    result.append(s)
    visited[s] = 1
    for i in G[s]:
        if not visited[i]:
            DFS(i, visited, G, result)


def T(G, s=0):
    size = len(G)
    visited = [0] * size
    GT = revert(G)
    stack = []
    result = []
    for i in range(size):
        if not visited[i]:
            DFSinv(i, visited, G, stack)
    for i in range(size):
        visited[i] = 0
    while len(stack):
        s = stack.pop()
        if not visited[s]:
            DFS(s, visited, G, result)
    return result
