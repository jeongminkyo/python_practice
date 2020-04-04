from collections import deque


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    queue.append(e)


n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
