maxInt = 1000000000000000


class Graph:

    def __init__(self, v, S):
        self.graph = [[] for i in range(v)]
        self.v = v
        self.source = S

    def addEdge(self, u, v, w):
        for e in self.graph[u]:
            if e[0] == v or e[0] == self.source-1:
                return
        self.graph[u].append([v, w])

    def BFS(self, s, t, parent):

        visited = [False] * self.v
        queue = []
        queue.append(s)
        visited[s] = True
        # Standard BFS Loop
        while queue:
            u = queue.pop(0)
            for e in self.graph[u]:

                if (not visited[e[0]]) and e[1] > 0:
                    queue.append(e[0])
                    visited[e[0]] = True
                    parent[e[0]] = u
                    if e[0] == t:
                        temp = e[0]
                        flowValue = float('inf')
                        while temp != s:
                            for k in self.graph[parent[temp]]:
                                if k[0] == temp:
                                    flowValue = min(flowValue, k[1])
                            temp = parent[temp]
                        # print(flowValue)
                        return flowValue
        return -1

    def minCut(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * self.v

        max_flow = 0  # There is no flow initially
        path_flow = self.BFS(source, sink, parent)
        # Augment the flow while there is path from source to sink
        while path_flow > 0:
            max_flow += path_flow
            # print(path_flow)
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                for k in self.graph[u]:
                    if k[0] == v:
                        k[1] -= path_flow
                for h in self.graph[v]:
                    if h[0] == u:
                        h[1] += path_flow
                v = parent[v]
            path_flow = self.BFS(source, sink, parent)

        return max_flow


def generateGraph(theMap, v, a, b, s):
    g = Graph(2 * v + 1, s)
    for i in range(a):
        for j in range(b):
            V1 = 2 * (i * b + j)
            V2 = V1 + 1
            value = theMap[i][j]
            if value>0:
                g.addEdge(V1, V2, value)
            if i > 0:
                # az u2 mire be v1 vase edge uv
                upNeighbour1 = 2 * ((i - 1) * b + j)
                # upNeighbour2 = upNeighbour1 + 1
                # g.addEdge(upNeighbour2, V1, maxInt)
                g.addEdge(V2, upNeighbour1, maxInt)
            if i < a - 1:
                downNeighbour1 = 2 * ((i + 1) * b + j)
                downNeighbour2 = downNeighbour1 + 1
                # g.addEdge(downNeighbour2, V1, maxInt)
                g.addEdge(V2, downNeighbour1, maxInt)
            if j > 0:
                leftNeighbour1 = 2 * (i * b + (j - 1))
                leftNeighbour2 = leftNeighbour1 + 1
                # g.addEdge(leftNeighbour2, V1, maxInt)
                g.addEdge(V2, leftNeighbour1, maxInt)
            if j < b - 1:
                rightNeighbour1 = 2 * (i * b + (j + 1))
                rightNeighbour2 = rightNeighbour1 + 1
                # g.addEdge(rightNeighbour2, V1, maxInt)
                g.addEdge(V2, rightNeighbour1, maxInt)
    t = a * b * 2
    for j in range(M):
        k = 2 * j + 1
        g.addEdge(k, t, maxInt)
        k += 2 * M * (N - 1)
        g.addEdge(k, t, maxInt)
    for i in range(N):
        k = 2 * (i * b) + 1
        g.addEdge(k, t, maxInt)
        k = 2 * (i * b) + 2 * (M - 1) + 1
        g.addEdge(k, t, maxInt)


    return g, t


def spiltWord(word):
    return [char for char in word]


def convert(line):
    temp = ""
    out = []
    intOut = []
    for l in line:
        if l != '  ':
            temp += l
    out = temp.split(' ')

    for o in out:
        if o != '':
            intOut.append(int(o))

    return intOut


while True:
    mn = input()
    mnLs = mn.split()
    N = int(mnLs[0])
    M = int(mnLs[1])
    i = 0
    if N == M == 0:
        break
    costMap = []

    for i in range(N):
        line = input()
        lineInt = convert(line)
        costMap.append(lineInt)

    nm = input()
    nmLs = nm.split(" ")
    n = int(nmLs[0])
    m = int(nmLs[1])
    sum = costMap[n-1][m]+costMap[n+1][m] + costMap[n][m-1] + costMap[n][m+1]
    source = 2 * n * M + 2 * (m - 1) + 1
    g, sink = generateGraph(costMap, M * N, N, M, source)
    mincut1 = g.minCut(source, sink)
    print(min(mincut1, costMap[n][m], sum))

