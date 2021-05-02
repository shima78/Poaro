def setFire(table, n, m, k, x, y):
    source = table[x][y]

    # Mark all the vertices as not visited
    visited = [False] * (m * n + 1)
    # Create a queue for BFS
    queue = []
    # Mark the source node as
    # visited and enqueue it
    queue.append(source)
    visited[source] = True
    row = 0
    col = 0
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        print(s, end=" ")

        currentT = s.time

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        adj = []
        if col > 0:
            adj.append(table[row][col - 1])
        if col + 1 < m:
            adj.append(table[row][col + 1])
        if row >0 :
            adj.append(table[row - 1][col])
            if col>0:
                adj.append(table[row - 1][col - 1])
            if col+1<m:
                adj.append(table[row - 1][col + 1])
        if row + 1 < n :
            adj.append(table[row + 1][col])
            if col > 0:
                adj.append(table[row + 1][col - 1])
            if col +1 < m:
                adj.append(table[row + 1][col + 1])

        for i in adj :
            if visited[i] == False:
                i.state = "f"
                if currentT + k < i.time :
                    i.time = currentT + k
                queue.append(i)
                visited[i]= True
