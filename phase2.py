from copy import deepcopy


def AllFired(N, M, Map):
    for i in range(0, N):
        for j in range(0, M):
            if Map[i][j] == '-':
                return False
    return True


def Search(N, M, Map, MarkMap, K):
    if AllFired(N, M, Map):
        return
    Fire(N, M, deepcopy(Map), MarkMap, K)
    x, y = Find(N, M, Map)
    return x, y


def Fire(N, M, Map, MarkMap, K):
    visited = [[False] * M for i in range(N)]
    queue = []
    row = 0
    col = 0

    visited[row][col] = True
    queue.append((row, col))
    while queue:
        e = queue.pop(0)
        row = e[0]
        col = e[1]

        currentTime = t[row][col]

        adj = []
        if col > 0:
            adj.append((row, col - 1))
        if col + 1 < M:
            adj.append((row, col + 1))
        if row > 0:
            adj.append((row - 1, col))
            if col > 0:
                adj.append((row - 1, col - 1))
            if col + 1 < M:
                adj.append((row - 1, col + 1))
        if row + 1 < N:
            adj.append((row + 1, col))
            if col > 0:
                adj.append((row + 1, col - 1))
            if col + 1 < M:
                adj.append((row + 1, col + 1))

        for element in adj:
            i = element[0]
            j = element[1]
            if currentTime + K < t[i][j]:
                t[i][j] = currentTime + K
                if Map[row][col] == 'f':
                    Map[i][j] = 'f'
                visited[i][j] = False
            if not visited[i][j]:
                queue.append(element)
                if Map[row][col] == 'f':
                    Map[i][j] = 'f'
                visited[i][j] = True

    return Map


def Find(N, M, Map):
    m = (0, 0, 0)
    for i in range(0, N):
        for j in range(0, M):
            if t[i][j] > m[2]:
                m = (i, j, t[i][j])
    return m[0], m[1]


def BFS(N, M, Map, MapMark, x, K):
    visited = [[False] * M for i in range(N)]

    xs, ys = FindPoaro(N, M, Map)
    xt, yt = FindT(N, M, Map)


    Path = [[0] * M for i in range(N)]

    queue = []
    queue.append((xs, ys))
    visited[xs][ys] = True

    while queue != []:
        e = queue.pop(0)
        if e[0] == xt and e[1] == yt:
            return Path[e[0]][e[1]]

        if e[1] - 1 >= 0:
            if MapMark[e[0]][e[1] - 1] > Path[e[0]][e[1]] + 1:
                if not visited[e[0]][e[1] - 1]:
                    visited[e[0]][e[1] - 1] = True
                    Path[e[0]][e[1] - 1] = Path[e[0]][e[1]] + 1
                    queue.append((e[0], e[1] - 1))
        if e[0] + 1 < N:
            if MapMark[e[0] + 1][e[1]] > Path[e[0]][e[1]] + 1:
                if not visited[e[0] + 1][e[1]]:
                    visited[e[0] + 1][e[1]] = True
                    Path[e[0] + 1][e[1]] = Path[e[0]][e[1]] + 1
                    queue.append((e[0] + 1, e[1]))
        if e[1] + 1 < M:
            if MapMark[e[0]][e[1] + 1] > Path[e[0]][e[1]] + 1:
                if not visited[e[0]][e[1] + 1]:
                    visited[e[0]][e[1] + 1] = True
                    Path[e[0]][e[1] + 1] = Path[e[0]][e[1]] + 1
                    queue.append((e[0], e[1] + 1))
        if e[0] - 1 >= 0:
            if MapMark[e[0] - 1][e[1]] > Path[e[0]][e[1]] + 1:
                if not visited[e[0] - 1][e[1]]:
                    visited[e[0] - 1][e[1]] = True
                    Path[e[0] - 1][e[1]] = Path[e[0]][e[1]] + 1
                    queue.append((e[0] - 1, e[1]))
    return "impossible"


def FindPoaro(N, M, Map):
    for i in range(0, N):
        for j in range(0, M):
            if (Map[i][j] == 's'):
                return i, j
    return -1, -1


def FindT(N, M, Map):
    for i in range(0, N):
        for j in range(0, M):
            if (Map[i][j] == 't'):
                return i, j
    return -1, -1



def spiltWord(word):
    return [char for char in word]

N = -1
M = -1
K = -1
ans = []
while not (N == 0 and M == 0 and K == 0):
    nmk = input()
    splitNMK = nmk.split(" ")
    N = int(splitNMK[0])
    M = int(splitNMK[1])
    K = int(splitNMK[2])
    if N==0 and M == 0 and K==0 :
        break
    a = []
    t = [[50000000000] * M for i in range(N)]
    i = 0
    for i in range(N):

        line = input()
        lineLs = spiltWord(line)
        a.append(lineLs)
        for j in range(M):
            if a[i][j] == 'f':
                t[i][j] = 0

    s = Search(N, M, a, t, K)
    g = BFS(N, M, a, t, 0, K)
    ans.append(g)
for a in ans:
    if a is not None:
        print(a)
