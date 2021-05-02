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


def spiltWord(word):
    return [char for char in word]


N = -1
M = -1
K = -1
while not (N == 0 and M == 0 and K == 0):
    nmk = input()
    splitNMK = nmk.split(" ")
    N = int(splitNMK[0])
    M = int(splitNMK[1])
    K = int(splitNMK[2])
    a = []
    t = [[50000000000] * M for i in range(N)]
    i = 0
    for i in range(N):

        line = input()
        lineLs = spiltWord(line)
        a.append(lineLs)
        flag = 0
        for j in range(M):
            if a[i][j] == 'f':
                flag = 1
                t[i][j] = 0
    s = None
    if flag == 1:
        s = Search(N, M, a, t, K)
    if s != None:
        print(s[0], s[1])
