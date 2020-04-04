def dfs(v):
    global sum
    sum += 1
    visited[v] = True

    for e in adj[v]:
        if not visited[e]:
            dfs(e)


n = int(input())
m = int(input())
sum = 0
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())

    adj[x].append(y)
    adj[y].append(x)

dfs(1)
print(sum-1)