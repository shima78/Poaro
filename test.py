maxInt = 10000000000000000


class Graph:
    def __init__(self, N, M):

        self.Alpha = None
        self.n = N + 1
        self.m = M + 1
        self.graph = [[maxInt] * self.n for i in range(self.n)]
        self.Trophy = [0 for i in range(self.n)]
        self.Dp = [0 for i in range(self.n)]

    def addEdge(self, u, v, E):
        self.graph[u][v] = E
        self.graph[v][u] = E

    def AddTrophy(self, T):
        for i in T:
            self.Trophy[i] = 1

    def AddAlpha(self, alpha):
        self.Alpha = alpha

    def FindIn(self, i, Matrix):
        for j in range(self.n):
            if self.graph[i][j] != 0:
                return Matrix[i][j]
        return 0

    def findHelper(self):
        Matrix, n = self.floyd_warshall()
        Trophy = self.count(n)
        self.Find(Matrix, Trophy, self.Alpha)

    def pick(self, s, mat, t, visit):
        index = -1
        val = maxInt
        i = 0
        for i in range(self.n):
            if t[s][i] > 0:
                ratio = mat[s][i] / t[s][i]
            if ratio < val:
                val = ratio
                index = i
        return index

    def Find(self):
        Matrix, n = self.floyd_warshall()
        Trophy = self.count(n)
        visit = [0 for i in range(self.n)]
        nextStop = self.pick(0, Matrix, Trophy, visit)
        visit[nextStop] = True
        numT = 0
        if nextStop >= 0:
            if self.Alpha - Matrix[0][nextStop] >= Matrix[nextStop][0]:
                self.Alpha -= Matrix[0][nextStop]
                numT += Trophy[0][nextStop]

        return MaxTreasure

    def floyd_warshall(self):
        next = [[None] * self.n for i in range(self.n)]
        distance = list(map(lambda i: list(map(lambda j: j, i)), self.graph))

        for i in range(self.n):
            for j in range(self.n):
                next[i][j] = i
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):

                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        next[i][j] = next[k][j]
        return distance, next

    def path(self, i, j, next, p):
        if i == j:
            p.append(i)
            return p
        elif next[i][j] is None:

            return p
        else:
            p.append(j)
            return self.path(i, next[i][j], next, p)

    def count(self, next):
        table = [[0] * self.n for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                pathh = []
                self.path(i, j, next, pathh)
                counter = 0
                for c in pathh:
                    counter += self.Trophy[c]
                table[i][j] = counter

        return table


NumTestCase = int(input())
while NumTestCase > 0:
    nm = input()
    splitNM = nm.split(" ")
    N = int(splitNM[0])
    M = int(splitNM[1])
    g = Graph(N, M)
    i = 0
    # ListOfTunnels = []
    for i in range(M):
        abc = input()
        ABC = abc.split()
        a = int(ABC[0])
        b = int(ABC[1])
        c = int(ABC[2])
        g.addEdge(a, b, c)
        # ListOfTunnels.append((a, b, c))

    numberOfTreasures = int(input())

    TreasureCavesStr = input().split(" ")
    TreasureCavesInt = [int(a) for a in TreasureCavesStr]
    g.AddTrophy(TreasureCavesInt)
    maxDist = int(input())
    g.AddAlpha(maxDist)
    # a,b = g.floyd_warshall()
    print(g.Find())
    NumTestCase -= 1
