import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if ground[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    count = 0
    ground = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        ground[x][y] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)