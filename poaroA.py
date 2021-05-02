from copy import deepcopy


def AllFired(N, M, Map):
    for i in range(0, N):
        for j in range(0, M):
            if Map[i][j] == '-':
                return False
    return True


def Search(N, M, Map, MarkMap, K, x):
    if AllFired(N, M, Map):
        return -1, -1
    Map2 = Fire(N, M, deepcopy(Map), MarkMap, x, K)
    x = x + K
    x, y = Search(N, M, Map2, MarkMap, K, x)
    if x == -1 and y == -1:
        x, y = Find(N, M, Map)
        return x, y
    return x, y



def Fire(N, M, Map, MarkMap, x, K):
    for i in range(0, N):
        for j in range(0, M):
            if Map[i][j] == 'f':
                if MarkMap[i][j] == x:
                    if i - 1 >= 0:
                        if Map[i - 1][j] == '-':
                            Map[i - 1][j] = 'f'
                            MarkMap[i - 1][j] = x + K

                    if i + 1 < N:
                        if Map[i + 1][j] == '-':
                            Map[i + 1][j] = 'f'
                            MarkMap[i + 1][j] = x + K

                    if j - 1 >= 0:
                        if Map[i][j - 1] == '-':
                            Map[i][j - 1] = 'f'
                            MarkMap[i][j - 1] = x + K

                    if j + 1 < M:
                        if Map[i][j + 1] == '-':
                            Map[i][j + 1] = 'f'
                            MarkMap[i][j + 1] = x + K

                    if i - 1 >= 0 and j - 1 >= 0:
                        if Map[i - 1][j - 1] == '-':
                            Map[i - 1][j - 1] = 'f'
                            MarkMap[i - 1][j - 1] = x + K

                    if i + 1 < N and j + 1 < M:
                        if Map[i + 1][j + 1] == '-':
                            Map[i + 1][j + 1] = 'f'
                            MarkMap[i + 1][j + 1] = x + K

                    if j - 1 >= 0 and i + 1 < N:
                        if Map[i + 1][j - 1] == '-':
                            Map[i + 1][j - 1] = 'f'
                            MarkMap[i + 1][j - 1] = x + K

                    if j + 1 < M and i - 1 >= 0:
                        if Map[i - 1][j + 1] == '-':
                            Map[i - 1][j + 1] = 'f'
                            MarkMap[i - 1][j + 1] = x + K
    for m in MarkMap:

        print(m)
    return Map


def Find(N, M, Map):
    for i in range(0, N):
        for j in range(0, M):
            if Map[i][j] == '-':
                return i, j
    return N, M


t = [[-1] * 4 for i in range(3)]
t[0][3] = 0
a = [['-', '-', '-', 'f'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]
s = Search(3, 4, a, t, 1, 0)
print(s)
t = [[-1] * 7 for i in range(7)]
t[0][0] = 0
t[1][1] = 0
t[1][5] = 0
t[2][4] = 0
t[4][6] = 0
t[6][5] = 0
a = [['f', '-', '-', '-', '-', '-', '-'], ['-', 'f', '-', '-', '-', 'f', '-'],
     ['-', '-', '-', '-', 'f', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'],
     ['-', '-', '-', '-', '-', '-', 'f'], ['-', '-', '-', '-', '-', '-', '-'],
     ['f', '-', '-', '-', '-', 'f', '-']]
s = Search(7, 7, a, t, 2, 0)
print(s)
