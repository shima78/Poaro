from collections import defaultdict


class Graph:
    def __init__(self, N, M):

        self.Alpha = None
        self.n = N + 1
        self.m = M + 1
        self.graph = [[0] * self.n for i in range(self.n)]
        self.Trophy = [0 * self.n for i in range(self.n)]

    def addEdge(self, u, v, E):
        self.graph[u][v] = E
        self.graph[v][u] = E

    def AddTrophy(self, T):
        for i in T:
            if (i != 0):
                self.Trophy[i] = 1
            else:
                self.Trophy[i] = 0

    def AddAlpha(self, alpha):
        self.Alpha = alpha

    def FindIn(self, i, Matrix):
        for j in range(self.n):
            if (self.graph[i][j] != 0):
                return Matrix[i][j]
        return 0

    def Find(self, Matrix, Trophy):
        MaxTreasure = 0
        index = 0
        for i in range(self.n):
            for j in range(self.n):
                if (Trophy[i][j] > MaxTreasure and Matrix[i][j] * 2 <= self.Alpha):
                    MaxTreasure = Trophy[i][j]
                else:
                    if (Trophy[i][j] > MaxTreasure and Matrix[i][j] * 2 > self.Alpha):
                        a = Graph.FindIn(self, j, Matrix)
                        if (a != 0):
                            if ((Matrix[i][j]) + a <= self.Alpha):
                                MaxTreasure = Trophy[i][j]
        return MaxTreasure

    def DynamicProgramming(self):
        DPMatrix = [[0] * self.n for i in range(self.n)]
        for i in range(self.n):
            DPMatrix[0][i] = self.graph[0][i]

        MaxTrophy = [[0] * self.n for i in range(self.n)]
        for i in range(self.n):
            MaxTrophy[0][i] = self.Trophy[i]
        Index = (0, 0)
        for i in range(1, self.n):
            for j in range(0, self.n):
                if (i > j and DPMatrix[i - 1][j + 1] != 0):
                    MaxTrophy[i][j] = MaxTrophy[i - 1][j + 1]
                    DPMatrix[i][j] = DPMatrix[i - 1][j + 1]
                    continue
                if (self.graph[i][j] != 0):
                    MaxTrophy[i][j] = MaxTrophy[i - 1][j - 1] + self.Trophy[j]
                    DPMatrix[i][j] = DPMatrix[i - 1][j - 1] + self.graph[i][j]
                else:
                    DPMatrix[i][j] = DPMatrix[i][j - 1]
                    MaxTrophy[i][j] = MaxTrophy[i][j - 1]

        print(Graph.Find(self, DPMatrix, MaxTrophy))


NumTestCase = int(input())
while NumTestCase > 0:
    nm = input()
    splitNM = nm.split(" ")
    N = int(splitNM[0])
    M = int(splitNM[1])
    g = Graph(N, M)
    i = 0
    ListOfTunnels = []
    for i in range(M):
        abc = input()
        ABC = abc.split()
        a = int(ABC[0])
        b = int(ABC[1])
        c = int(ABC[2])
        g.addEdge(a, b, c)
        ListOfTunnels.append((a, b, c))

    numberOfTreasures = int(input())

    TreasureCavesStr = input().split(" ")
    TreasureCavesInt = [int(a) for a in TreasureCavesStr]
    g.AddTrophy(TreasureCavesInt)
    maxDist = int(input())
    g.AddAlpha(maxDist)
    NumTestCase -= 1
    g.DynamicProgramming()